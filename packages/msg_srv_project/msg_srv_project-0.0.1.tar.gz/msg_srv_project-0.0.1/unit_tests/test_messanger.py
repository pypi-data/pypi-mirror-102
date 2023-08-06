import os
import subprocess
import sys
import unittest
from client import msg_parser
from common.constant import RESPONSE, ERROR, ACCOUNT_NAME, TIME, PRESENCE, DEF_IP, DEF_PORT, ACTION, USER
from common.messanger import Message, Connector, args


class Tests(unittest.TestCase):
    def setUp(self):
        self.server_process = subprocess.Popen('python ../server.py', creationflags=subprocess.CREATE_NEW_CONSOLE)
        self.conn1 = Connector('client')

    def tearDown(self):
        self.conn1.close()
        self.server_process.kill()

    def __del__(self):
        self.conn1.close()
        self.server_process.kill()

    def test_no_connection(self):
        with self.assertRaises(ConnectionRefusedError):
            self.conn1 = Connector('client', port=1717)
        print('test_no_connection - OK')

    def test_incorrect_port(self):
        with self.assertRaises(SystemExit):
            self.conn1 = Connector('client', port=171)
        with self.assertRaises(SystemExit):
            self.conn1 = Connector('server', port=171)

    def test_args(self):
        print(sys.argv[0])
        # ---------------------------------------
        addr, port = args()
        self.assertEqual((addr, port), (DEF_IP, DEF_PORT))
        print('1-OK')
        # ---------------------------------------
        sys.argv.append('1717')
        addr, port = args()
        self.assertEqual((addr, port), (DEF_IP, 1717))
        print('2-OK')
        # ---------------------------------------
        sys.argv[1] = '192.168.0.11'
        addr, port = args()
        self.assertEqual((addr, port), ('192.168.0.11', DEF_PORT))
        print('3-OK')
        # ---------------------------------------
        sys.argv[1] = '1717'
        sys.argv.append('192.168.0.11')
        addr, port = args()
        self.assertEqual((addr, port), ('192.168.0.11', 1717))
        print('4-OK')
        # ---------------------------------------
        sys.argv[1] = '192.168.0.11'
        sys.argv[2] = '1717'
        self.assertEqual((addr, port), ('192.168.0.11', 1717))
        print('5-OK')


if __name__ == '__main__':
    unittest.main()
