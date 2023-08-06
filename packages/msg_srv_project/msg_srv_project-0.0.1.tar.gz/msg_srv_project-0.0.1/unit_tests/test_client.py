import os
import subprocess
import sys
import unittest
from client import msg_parser
from common.constant import RESPONSE, ERROR, ACCOUNT_NAME, TIME, PRESENCE, DEF_IP, DEF_PORT, ACTION, USER
from common.messanger import Message, Connector, args


class TestsClient(unittest.TestCase):
    test_presence_msg = {
        ACTION: PRESENCE,
        TIME: 1.1,
        USER: {ACCOUNT_NAME: 'Guest'}
    }
    test_resp_ok_msg = {RESPONSE: 200}
    test_resp_err_msg = {RESPONSE: 400, ERROR: 'Bad Request'}

    def test_client_msg_parser_200(self):
        self.assertEqual('200 : OK', msg_parser(self.test_resp_ok_msg))

    def test_client_msg_parser_400(self):
        self.assertEqual('400 : Bad Request', msg_parser(self.test_resp_err_msg))

    def test_client_msg_parser_err(self):
        with self.assertRaises(ValueError):
            msg_parser(self.test_presence_msg)


if __name__ == '__main__':
    unittest.main()
