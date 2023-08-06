import argparse
import json
import sys
from socket import *
import time
import logging
import server_dist.log.configs.server_log_conf
from server_dist.common.constant import ACTION, ENCODING, TIME, USER, \
    ACCOUNT_NAME, MAX_PACKAGE_LENGTH, RESPONSE, ERROR, DEF_PORT, DEF_IP, MESSAGE_TEXT, SENDER, DESTINATION, LIST_INFO, \
    ADD_CONTACT, CONTACT_NAME, REMOVE_CONTACT, PRESENCE, PUBLIC_KEY, DATA, PUBLIC_KEY_REQUEST
from server_dist.common.decorators import log_decorator
from server_dist.common.descriptors import PortValue, AddrValue
from server_dist.common.meta import Verifier

SRV_LOGGER = logging.getLogger('server')
#CLN_LOGGER = logging.getLogger('client')


def srv_database_request(connector, username, request_type, contact_name=None):
    #CLN_LOGGER.debug(f'Data request for {username}')
    msg = Message(request_type, account_name=username, contact=contact_name)
    msg.send_msg(connector)
    # print(request_type)
    if request_type not in [ADD_CONTACT, REMOVE_CONTACT]:
        return msg_parser(connector.get_msg())
    else:
        return 'OK'


@log_decorator
def msg_parser(msg):
    #CLN_LOGGER.debug(f'parser input msg: {msg}')
    if RESPONSE in msg:
        if msg[RESPONSE] == 200:
            #CLN_LOGGER.debug(f'parser output msg is "200 : OK"')
            return '200 : OK'
        elif msg[RESPONSE] == 202:
            return msg[LIST_INFO]
        else:
            err = msg[ERROR] if msg[ERROR] else 'unknown error!'
            #CLN_LOGGER.debug(f'parser output msg is "400 : {err}"')
            return f'400 : {err}'
    elif MESSAGE_TEXT in msg:
        return f'{time.ctime()} {msg[SENDER]}: {msg[MESSAGE_TEXT]}'
    raise ValueError


@log_decorator
def args2(def_ip, def_port):
    args = argparse.ArgumentParser()
    args.add_argument('port', default=def_port, type=int, nargs='?')
    args.add_argument('addr', default=def_ip, nargs='?')
    args.add_argument('-m', default='listen', nargs='?')
    args.add_argument('-n', default=None, nargs='?')
    args.add_argument('-p', '--password', default='', nargs='?')
    formatter = args.parse_args(sys.argv[1:])
    addr, port, mode, name, password = formatter.addr, formatter.port, formatter.m, formatter.n, formatter.password
    return addr, port, mode, name, password


class Connector(metaclass=Verifier):
    port = PortValue()
    address = AddrValue()

    # @log_decorator
    def __init__(self, type, address=DEF_IP, port=DEF_PORT):
        self.s = socket(AF_INET, SOCK_STREAM)  # создаем сокет TCP
        self.port = port
        self.type = type
        self.clients = {}
        self.address = address

        '''
        try:
            if self.port < 1024 or self.port > 65535:
                raise ValueError
        except ValueError:
            print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
            if type == 'server':
                SRV_LOGGER.debug(f'incorrect port {self.port}')
            elif type == 'client':
                CLN_LOGGER.debug(f'incorrect port {self.port}')
            sys.exit(1)

        if type == 'server':
            # print('server')
            self.s.bind((self.address, self.port))
            self.s.settimeout(1)
            self.s.listen(5)
            SRV_LOGGER.debug(f'bind successful! addr {self.address}, port {self.port}')
            SRV_LOGGER.debug(f'Запущен сервер по адресу {self.address} порт {self.port}')
        elif type == 'client':
            # print('client')
            self.s.connect((self.address, self.port))  # Соединиться с сервером
            CLN_LOGGER.debug(f'client connect successful! addr {self.address}, port {self.port}')
            '''
        # try:

        # except ConnectionRefusedError:
        # print('No connection!')

    def connect(self):
        self.s.connect((self.address, self.port))  # Соединиться с сервером
        # CLN_LOGGER.debug(f'client connect successful! addr {self.address}, port {self.port}')

    def bind(self):
        self.s.bind((self.address, self.port))
        self.s.settimeout(1)
        SRV_LOGGER.debug(
            f'bind successful! addr {self.address}, port {self.port}')
        SRV_LOGGER.debug(
            f'Запущен сервер по адресу {self.address} порт {self.port}')

    def listen(self):
        self.s.listen(5)

    def __del__(self):
        self.s.close()
        # CLN_LOGGER.debug(f'connection closed')
        # SRV_LOGGER.debug(f'connection closed')

    @log_decorator
    def get_msg(self, client_obj=None):
        if self.type == 'client':
            encoded_response = self.s.recv(MAX_PACKAGE_LENGTH)
            # print('ok')
        elif self.type == 'server':
            encoded_response = client_obj.recv(MAX_PACKAGE_LENGTH)

        # print('ok')
        if isinstance(encoded_response, bytes):
            json_response = encoded_response.decode(ENCODING)
            response = json.loads(json_response)
            if isinstance(response, dict):
                return response
            raise ValueError
        raise ValueError

    @log_decorator
    def close(self):
        self.s.close()
        #f self.type == 'client':
            #CLN_LOGGER.debug(f'connection closed {self.address}')
        if self.type == 'server':
            SRV_LOGGER.debug(f'connection closed {self.address}')
        if self.clients:
            for client in self.clients:
                self.client.close()
            SRV_LOGGER.debug(f'client connection closed')

    # @log_decorator
    def accept(self):
        try:
            next_client, next_address = self.s.accept()
        except OSError:
            pass
        else:
            self.clients[next_client] = next_address
            SRV_LOGGER.debug(f'connection accepted from {next_address}')

    # def getpeername1(self, client_obj=None):
    # client_obj.getpeername()


class Message:
    def __init__(
            self,
            action=None,
            account_name='Guest',
            response=None,
            response_code=None,
            error=None,
            text=None,
            sender=None,
            to=None,
            data_list=None,
            contact=None,
            pubkey=None,
            bin=None):
        self.action = action
        self.time = time
        self.response = response
        self.account_name = account_name
        self.response_code = response_code
        self.error = error
        self.text = text
        self.sender = sender
        self.to = to
        self.message = {}
        self.data_list = data_list
        self.contact = contact
        self.pubkey = pubkey
        self.bin = bin

        if action is not None:
            self.message = {
                ACTION: self.action,
                TIME: time.ctime(),
                USER: {ACCOUNT_NAME: self.account_name}
            }
            if text is not None:
                self.message[MESSAGE_TEXT] = self.text
            if sender is not None:
                self.message[SENDER] = self.sender
            if to is not None:
                self.message[DESTINATION] = self.to
            if action == ADD_CONTACT or action == REMOVE_CONTACT or action == PUBLIC_KEY_REQUEST:
                self.message[USER][CONTACT_NAME] = self.contact
            if action == PRESENCE and pubkey is not None:
                self.message[USER][PUBLIC_KEY] = self.pubkey
            if action == RESPONSE and response_code == 511:
                self.message[DATA] = self.bin
                self.message[RESPONSE] = self.response_code

        else:
            self.message = {RESPONSE: self.response_code}
            if response_code == 400:
                self.message[ERROR] = self.error
            if response_code == 202:
                self.message[LIST_INFO] = self.data_list
            if response_code == 511:
                self.message[DATA] = self.bin

    @log_decorator
    def send_msg(self, connector_obj, client_obj=None):
        js_message = json.dumps(self.message)
        encoded_message = js_message.encode(ENCODING)
        try:
            if connector_obj.type == 'client':
                connector_obj.s.send(encoded_message)
            elif connector_obj.type == 'server':
                client_obj.send(encoded_message)
            return 0
        except BaseException:
            return -1
