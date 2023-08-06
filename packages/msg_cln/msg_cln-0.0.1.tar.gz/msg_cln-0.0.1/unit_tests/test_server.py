import os
import subprocess
import sys
import unittest
from client import msg_parser
from common.constant import RESPONSE, ERROR, ACCOUNT_NAME, TIME, PRESENCE, DEF_IP, DEF_PORT, ACTION, USER
from common.messanger import Message, Connector, args


class TestServer(unittest.TestCase):
    def setUp(self):
        self.server_process = subprocess.Popen('python ../server.py', creationflags=subprocess.CREATE_NEW_CONSOLE)
        self.conn1 = Connector('client')
        self.msg_from_client = Message(PRESENCE)
        self.msg_from_client1 = Message(PRESENCE, account_name='Guest1')

    def tearDown(self):
        self.conn1.close()
        self.server_process.kill()

    def __del__(self):
        self.conn1.close()
        self.server_process.kill()

    def test_send_msg(self):
        self.assertEqual(0, self.msg_from_client.send_msg(self.conn1))
        print('test_send_msg - OK')

    def test_get_msg_presence(self):
        conn_srv = Connector('server', port=1717)
        conn_client = Connector('client', port=1717)
        self.msg_from_client.send_msg(conn_client)
        conn_srv.accept()
        msg_from_client = conn_srv.get_msg()
        msg_from_client[TIME] = 1.1
        self.assertEqual({'action': PRESENCE,
                          'time': 1.1,
                          'user': {ACCOUNT_NAME: 'Guest'}}, msg_from_client)
        conn_srv.close()
        conn_client.close()
        print('test_get_msg_presence - OK')

    def test_get_msg_200(self):
        self.msg_from_client.send_msg(self.conn1)
        msg2 = self.conn1.get_msg()
        self.assertEqual({RESPONSE: 200}, msg2)
        print('test_get_msg_200 - OK')

    def test_get_msg_400(self):
        self.msg_from_client1.send_msg(self.conn1)
        msg2 = self.conn1.get_msg()
        self.assertEqual({ERROR: 'Bad Request', RESPONSE: 400}, msg2)
        print('test_get_msg_400 - OK')

if __name__ == '__main__':
    unittest.main()
