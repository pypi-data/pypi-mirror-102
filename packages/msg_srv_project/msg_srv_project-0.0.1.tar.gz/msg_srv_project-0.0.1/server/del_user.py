import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog
# from server_dist.common.constant import ADD_CONTACT, USERS_REQUEST
# from server_dist.common.messenger import srv_database_request


class DelUserDialog(QDialog):
    def __init__(self, srv_db):
        super().__init__()
        uic.loadUi('server/del_user.ui', self)
        self.srv_db = srv_db
        self.btnCancel.clicked.connect(self.close)
        # self.actionExit.triggered.connect(qApp.quit)
        # self.btnAdd.clicked.connect(self.add_cont_func)
        self.btnDel.clicked.connect(self.delete_user)
        self.show()
        self.all_users_fill()

    def all_users_fill(self):
        self.comboBox.addItems([item[0] for item in self.srv_db.user_list()])

    def delete_user(self):
        self.srv_db.del_user(self.comboBox.currentText())
        '''
        if self.selector.currentText() in self.server.names:
            sock = self.server.names[self.selector.currentText()]
            del self.server.names[self.selector.currentText()]
            self.server.remove_client(sock)
        # Рассылаем клиентам сообщение о необходимости обновить справочники
        self.server.service_update_lists()
        '''
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DelUserDialog()
    # ex.text1.append('qweqweqwe')
    # ex.text1.append('qweqweqwe2')
    # dial = ConfigWindow()
    app.exec_()
