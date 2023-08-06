import sys

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon, QTextCursor
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QAction, qApp, QTableView, QPushButton, QLineEdit, \
    QFileDialog, QDialog, QTextEdit

# GUI - Создание таблицы QModel, для отображения в окне программы.
# from add_user import RegisterUser
from server_dist.server.del_user import DelUserDialog
from server_dist.server.add_user import RegisterUser
from server_dist.server.srv_db import ServerDB


def gui_create_model(srv_db):
    list_users = srv_db.active_user_list()
    lst1 = QStandardItemModel()
    lst1.setHorizontalHeaderLabels(
        ['username', 'IP', 'port', 'connection time'])
    for row in list_users:
        user, ip, port, time = row
        user = QStandardItem(user)
        ip = QStandardItem(ip)
        port = QStandardItem(str(port))
        time = QStandardItem(str(time))
        # user.setEditable(False)
        lst1.appendRow([user, ip, port, time])
    return lst1


class MainWindow(QMainWindow):
    def __init__(self, ip, port, srv_db):
        super().__init__()
        self.ip = ip
        self.port = port
        self.srv_db = srv_db
        exitqAction = QAction(QIcon('server/exit.jpg'), '&Exit', self)
        exitqAction.triggered.connect(qApp.quit)

        self.refresh_button = QAction(
            QIcon('server/refresh.jpg'), '&Refresh', self)
        self.config_btn = QAction(
            QIcon('server/settings.jpg'), '&Settings', self)
        # self.show_history_button = QAction('History', self)
        self.register_btn = QAction(
            QIcon('server/Add_user_icon_blue.svg.png'),
            '&Регистрация пользователя',
            self)
        self.remove_btn = QAction(
            QIcon('server/remove-user-icon.png'),
            '&Удаление пользователя',
            self)

        self.statusBar()

        self.toolbar = self.addToolBar('MainBar')
        self.toolbar.addAction(exitqAction)
        self.toolbar.addAction(self.refresh_button)
        # self.toolbar.addAction(self.show_history_button)
        self.toolbar.addAction(self.config_btn)
        self.toolbar.addAction(self.register_btn)
        self.toolbar.addAction(self.remove_btn)

        self.setFixedSize(800, 700)
        self.setWindowTitle(f'Server {ip}:{port}')

        self.label = QLabel('Active users:', self)
        self.label.setFixedSize(240, 15)
        self.label.move(10, 40)

        self.active_clients_table = QTableView(self)
        self.active_clients_table.move(10, 55)
        self.active_clients_table.setFixedSize(780, 400)

        self.label2 = QLabel('Log:', self)
        self.label2.setFixedSize(240, 20)
        self.label2.move(10, 475)

        self.text1 = QTextEdit(self)
        self.text1.move(10, 500)
        self.text1.setFixedSize(780, 180)

        c = self.text1.textCursor()
        c.movePosition(QTextCursor.End)
        self.text1.setTextCursor(c)

        self.register_btn.triggered.connect(self.reg_user)
        self.remove_btn.triggered.connect(self.del_user)
        self.show()

    def reg_user(self):
        global reg_window
        reg_window = RegisterUser(self.srv_db)
        reg_window.show()

    def del_user(self):
        global rem_window
        rem_window = DelUserDialog(self.srv_db)
        rem_window.show()


class ConfigWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(380, 260)
        self.setWindowTitle('Настройки сервера')

        # Надпись о файле базы данных:
        self.db_path_label = QLabel('Путь до файла базы данных: ', self)
        self.db_path_label.move(10, 10)
        self.db_path_label.setFixedSize(240, 15)

        # Строка с путём базы
        self.db_path = QLineEdit(self)
        self.db_path.setFixedSize(250, 20)
        self.db_path.move(10, 30)
        self.db_path.setReadOnly(True)

        # Кнопка выбора пути.
        self.db_path_select = QPushButton('Обзор...', self)
        self.db_path_select.move(275, 28)

        # Функция обработчик открытия окна выбора папки
        def open_file_dialog():
            # global dialog
            dialog = QFileDialog(self)
            path = dialog.getExistingDirectory()
            path = path.replace('/', '\\')
            self.db_path.insert(path)

        self.db_path_select.clicked.connect(open_file_dialog)

        # Метка с именем поля файла базы данных
        self.db_file_label = QLabel('Имя файла базы данных: ', self)
        self.db_file_label.move(10, 68)
        self.db_file_label.setFixedSize(180, 15)

        # Поле для ввода имени файла
        self.db_file = QLineEdit(self)
        self.db_file.move(200, 66)
        self.db_file.setFixedSize(150, 20)

        # Метка с номером порта
        self.port_label = QLabel('Номер порта для соединений:', self)
        self.port_label.move(10, 108)
        self.port_label.setFixedSize(180, 15)

        # Поле для ввода номера порта
        self.port = QLineEdit(self)
        self.port.move(200, 108)
        self.port.setFixedSize(150, 20)

        # Метка с адресом для соединений
        self.ip_label = QLabel('С какого IP принимаем соединения:', self)
        self.ip_label.move(10, 148)
        self.ip_label.setFixedSize(180, 15)

        # Метка с напоминанием о пустом поле.
        self.ip_label_note = QLabel(
            ' оставьте это поле пустым, чтобы\n принимать соединения с любых адресов.',
            self)
        self.ip_label_note.move(10, 168)
        self.ip_label_note.setFixedSize(500, 30)

        # Поле для ввода ip
        self.ip = QLineEdit(self)
        self.ip.move(200, 148)
        self.ip.setFixedSize(150, 20)

        # Кнопка сохранения настроек
        self.save_btn = QPushButton('Save', self)
        self.save_btn.move(190, 220)

        # Кнапка закрытия окна
        self.close_button = QPushButton('Close', self)
        self.close_button.move(275, 220)
        self.close_button.clicked.connect(self.close)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    srv_db = ServerDB()
    ex = MainWindow('192.188.1.1', '2323', srv_db)
    # ex.text1.append('qweqweqwe')
    # ex.text1.append('qweqweqwe2')
    # dial = ConfigWindow()
    app.exec_()
