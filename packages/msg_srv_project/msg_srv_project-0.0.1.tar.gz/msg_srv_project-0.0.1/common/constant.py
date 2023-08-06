# Константы
import logging

DEF_PORT = 7777
DEF_IP = '127.0.0.1'
MAX_CONNECTIONS = 5  # максимальная очередь подключений
MAX_PACKAGE_LENGTH = 1024  # максимальная длинна сообщения в байтах
ENCODING = 'utf-8'
LOGGING_LEVEL = logging.DEBUG
SERVER_DATABASE = 'sqlite:///server/srv_database.db3'

# for JIM :
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
MESSAGE = 'message'
MESSAGE_TEXT = 'text'
SENDER = 'sender'
EXIT = 'exit'
DESTINATION = 'to'
GET_CONTACTS = 'get_contacts'
LIST_INFO = 'data_list'
REMOVE_CONTACT = 'remove'
ADD_CONTACT = 'add'
USERS_REQUEST = 'get_users'
CONTACT_NAME = 'contact'
DATA = 'bin'
PUBLIC_KEY = 'pubkey'
USERS_REQUEST = 'get_users'
PUBLIC_KEY_REQUEST = 'pubkey_need'
