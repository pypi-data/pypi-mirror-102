import binascii
import hashlib
# import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, qApp, QApplication, QMainWindow, QDialog, QLineEdit, QMessageBox


# from server_dist.common.constant import ADD_CONTACT, USERS_REQUEST
# from server_dist.common.messenger import srv_database_request


class RegisterUser(QDialog):
    def __init__(self, srv_db):
        super().__init__()
        uic.loadUi('server/add_user.ui', self)
        self.btnExit.clicked.connect(self.close)
        # self.actionExit.triggered.connect(qApp.quit)
        # self.btnAdd.clicked.connect(self.add_cont_func)
        self.srv_db = srv_db
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.btnSave.clicked.connect(self.save_data)
        self.messages = QMessageBox()
        self.show()

    def save_data(self):
        if not self.lineEdit.text():
            self.messages.critical(
                self, 'ERROR!!!', 'Не указано имя пользователя.')
            return
        elif self.lineEdit_2.text() != self.lineEdit_3.text():
            self.messages.critical(
                self, 'ERROR!!!', 'Введённые пароли не совпадают.')
            return
        elif self.srv_db.check_user(self.lineEdit.text()):
            self.messages.critical(
                self, 'ERROR!!!', 'Имя пользователя уже занято')
            return
        else:
            # print('start adding user')
            passwd_bytes = self.lineEdit_2.text().encode('utf-8')
            salt = self.lineEdit.text().lower().encode('utf-8')
            passwd_hash = hashlib.pbkdf2_hmac(
                'sha512', passwd_bytes, salt, 10000)
            # print(passwd_hash)
            self.srv_db.add_user(
                self.lineEdit.text(),
                binascii.hexlify(passwd_hash))
            self.messages.information(
                self, 'OK!', 'Пользователь успешно зарегистрирован')
            # Рассылаем клиентам сообщение о необходимости обновить справочники
            # self.server.service_update_lists()
            self.close()
