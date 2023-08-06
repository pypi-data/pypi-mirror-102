from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Table, MetaData, Text
from sqlalchemy.orm import sessionmaker, mapper
from sqlalchemy.sql import default_comparator
from server_dist.common.constant import SERVER_DATABASE



class ServerDB:
    class Users:
        def __init__(self, login_name, passwd_hash):
            self.user_id = None
            self.login_name = login_name
            self.last_login = datetime.now()
            self.passwd_hash = passwd_hash
            self.pubkey = None

    class ActiveUsr:
        def __init__(self, user_id, addr, port, login_time):
            # self.id = None
            self.user_id = user_id
            self.addr = addr
            self.port = port
            self.login_time = login_time

    class SrvHist:
        def __init__(self, user_id, date, addr, port):
            self.id = None
            self.user_id = user_id
            self.date_time = date
            self.addr = addr
            self.port = port

    class UsrContacts:
        def __init__(self, user, contact):
            self.id = None
            self.user = user
            self.contact = contact

    class UsrHist:
        def __init__(self, user_id):
            # self.id = None
            self.user_id = user_id
            self.sent = 0
            self.accepted = 0

    def __init__(self):
        self.database_engine = create_engine(
            SERVER_DATABASE, echo=False, pool_recycle=3600, connect_args={
                'check_same_thread': False})  # 1 hour
        self.metadata = MetaData()

        users_table = Table('Users', self.metadata,
                            Column('user_id', Integer, primary_key=True),
                            Column('login_name', String, unique=True),
                            Column('last_login', DateTime),
                            Column('passwd_hash', String),
                            Column('pubkey', Text)
                            )

        active_users_table = Table('ActiveUsr', self.metadata,
                                   # Column('id', Integer, primary_key=True),
                                   Column(
                                       'user_id', ForeignKey('Users.user_id'), primary_key=True),
                                   Column('addr', String),
                                   Column('port', Integer),
                                   Column('login_time', DateTime)
                                   )

        user_login_history = Table(
            'SrvHist', self.metadata, Column(
                'id', Integer, primary_key=True), Column(
                'user_id', ForeignKey('Users.user_id')), Column(
                'date_time', DateTime), Column(
                    'addr', String), Column(
                        'port', String))

        usr_contacts = Table('UsrContacts', self.metadata,
                             Column('id', Integer, primary_key=True),
                             Column('user', ForeignKey('Users.user_id')),
                             Column('contact', ForeignKey('Users.user_id'))
                             )

        usr_hist = Table('UsrHist', self.metadata,
                         # Column('id', Integer, primary_key=True),
                         Column(
                             'user_id',
                             ForeignKey('Users.user_id'),
                             primary_key=True),
                         Column('sent', Integer),
                         Column('accepted', Integer)
                         )

        self.metadata.create_all(self.database_engine)

        mapper(self.Users, users_table)
        mapper(self.ActiveUsr, active_users_table)
        mapper(self.SrvHist, user_login_history)
        mapper(self.UsrContacts, usr_contacts)
        mapper(self.UsrHist, usr_hist)

        Session = sessionmaker(bind=self.database_engine)
        self.session = Session()

        self.session.query(self.ActiveUsr).delete()
        self.session.commit()

    def add_user(self, name, passwd_hash):
        user_row = self.Users(name, passwd_hash)
        self.session.add(user_row)
        self.session.commit()
        history_row = self.UsrHist(user_row.user_id)
        self.session.add(history_row)
        self.session.commit()

    def del_user(self, name):
        user = self.session.query(
            self.Users).filter_by(
            login_name=name).first()
        self.session.query(
            self.ActiveUsr).filter_by(
            user_id=user.user_id).delete()
        self.session.query(
            self.SrvHist).filter_by(
            user_id=user.user_id).delete()
        self.session.query(
            self.UsrContacts).filter_by(
            user=user.user_id).delete()
        self.session.query(
            self.UsrContacts).filter_by(
            contact=user.user_id).delete()
        self.session.query(
            self.SrvHist).filter_by(
            user_id=user.user_id).delete()
        self.session.query(self.Users).filter_by(login_name=name).delete()
        self.session.commit()

    def check_user(self, name):
        if self.session.query(self.Users).filter_by(login_name=name).count():
            return True
        else:
            return False

    def srv_get_pubkey(self, name):
        user = self.session.query(
            self.Users).filter_by(
            login_name=name).first()
        return user.pubkey

    def srv_get_hash(self, name):
        user = self.session.query(
            self.Users).filter_by(
            login_name=name).first()
        return user.passwd_hash

    def srv_login(self, login_name, addr, port, key):
        Session1 = sessionmaker(bind=self.database_engine)
        session1 = Session1()
        query = session1.query(self.Users).filter_by(login_name=login_name)
        user = query.first()
        if user:
            user.last_login = datetime.now()
            if user.pubkey != key:
                user.pubkey = key
        else:
            user = self.Users(login_name)
            session1.add(user)
            session1.commit()  # чтобы user_id присвоился и мы запхали его в остальные таблицы
            # добавляем сразу запись в usr_hist
            session1.add(self.UsrHist(user.user_id))

        new_active_user = self.ActiveUsr(
            user.user_id, addr, port, datetime.now())
        session1.add(new_active_user)

        new_history_record = self.SrvHist(
            user.user_id, datetime.now(), addr, port)
        session1.add(new_history_record)

        session1.commit()

    def logout(self, username):
        user = self.session.query(
            self.Users).filter_by(
            login_name=username).first()
        self.session.query(
            self.ActiveUsr).filter_by(
            user_id=user.user_id).delete()
        # query = self.session.query(self.ActiveUsr).join(self.Users, self.Users.user_id == self.ActiveUsr.user_id)\
        #   .filter_by(login_name=username)
        # print(query)
        self.session.commit()

    def upd_usr_hist(self, sender_name, destination_usr_name):
        sender = self.session.query(
            self.Users).filter_by(
            login_name=sender_name).first().user_id
        recipient = self.session.query(
            self.Users).filter_by(
            login_name=destination_usr_name).first()
        # print(recipient)
        if recipient:
            recipient_row = self.session.query(
                self.UsrHist).filter_by(
                user_id=recipient.user_id).first()
            recipient_row.accepted += 1

        sender_row = self.session.query(
            self.UsrHist).filter_by(
            user_id=sender).first()
        sender_row.sent += 1
        self.session.commit()

    def upd_usr_contact(self, user, contact, action):
        try:
            user_id = self.session.query(
                self.Users).filter_by(
                login_name=user).first().user_id
            contact_id = self.session.query(
                self.Users).filter_by(
                login_name=contact).first().user_id
            contact_query = self.session.query(
                self.UsrContacts).filter_by(
                user=user_id, contact=contact_id)
            if action == 'add' and contact_query.first() is None:
                self.session.add(self.UsrContacts(user_id, contact_id))
            elif action == 'del':
                contact_query.delete()
            else:
                pass

            self.session.commit()
        except BaseException:
            print(f'contact not exists')

    def user_list(self):
        Session1 = sessionmaker(bind=self.database_engine)
        session1 = Session1()
        return session1.query(
            self.Users.login_name,
            self.Users.last_login).all()

    def active_user_list(self):
        Session1 = sessionmaker(bind=self.database_engine)
        session1 = Session1()
        return session1.query(
            self.Users.login_name,
            self.ActiveUsr.addr,
            self.ActiveUsr.port,
            self.ActiveUsr.login_time) .join(
            self.Users,
            self.Users.user_id == self.ActiveUsr.user_id).all()

    def get_srv_hist(self, username=None):
        Session1 = sessionmaker(bind=self.database_engine)
        session1 = Session1()
        query = session1.query(
            self.Users.login_name,
            self.SrvHist.addr,
            self.SrvHist.port,
            self.SrvHist.date_time,
        ).join(
            self.Users,
            self.Users.user_id == self.SrvHist.user_id)
        return query.filter(self.Users.login_name ==
                            username).all() if username else query.all()

    def get_contacts(self, username=None):
        Session1 = sessionmaker(bind=self.database_engine)
        session1 = Session1()

        query = session1.query(self.UsrContacts, self.Users.login_name). \
            join(self.Users, self.UsrContacts.contact == self.Users.user_id)
        if username:
            user_id = session1.query(
                self.Users).filter_by(
                login_name=username).first().user_id
            return [contact[1] for contact in query.filter(
                self.UsrContacts.user == user_id).all()]
        else:
            return [contact[1] for contact in query.all()]

    def get_usr_hist(self, username=None):
        Session1 = sessionmaker(bind=self.database_engine)
        session1 = Session1()
        query = session1.query(
            self.Users.login_name,
            self.Users.last_login,
            self.UsrHist.sent,
            self.UsrHist.accepted
        ).join(self.Users, self.Users.user_id == self.UsrHist.user_id)
        # print(query.all())
        return query.filter(self.Users.login_name ==
                            username).all() if username else query.all()


# Отладка
if __name__ == '__main__':
    test_db = ServerDB()
    '''
    print(test_db.user_list())
    test_db.login('client_4', '192.168.1.4', 8888)
    test_db.login('client_2', '192.168.1.5', 7777)
    test_db.logout('client_2')
    print(test_db.active_user_list())
    print(test_db.history('client_4'))
    print(test_db.history())
'''
   # test_db.srv_login('client_4', '192.168.1.4', 8888)
   # test_db.srv_login('client_2', '192.168.1.5', 7777)
    #test_db.upd_usr_contact('client_2', 'client_4', action='add')
    #test_db.upd_usr_contact('client_2', 'client_2', action='add')
    #test_db.upd_usr_contact('client_4', 'client_4', action='add')
    #test_db.upd_usr_contact('client_4', 'client_2', action='add')
    # print(test_db.get_usr_hist())
    # print(test_db.get_contacts('client_2'))
    #test_db.upd_usr_hist('user44', 'user999')
