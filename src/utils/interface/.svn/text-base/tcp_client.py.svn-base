# -*- coding: utf-8 -*-
"""用来向tcp端口发送数据并得到返回信息。

class:

    TCPClient  -- 模拟tcp客户端，向服务器端发送信息并获取返回值

    methods:

        connect  -- 连接服务器端
        send  -- 发送信息
        close  -- 关闭连接

"""
import socket
from src.utils.logger import Logger


class TCPClient(object):

    def __init__(self, domain, port):
        self.logger = Logger(__name__).get_logger()

        self.domain = domain
        self.port = port
        self.flag = 0  # 连接后置为1
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """连接指定IP、端口"""
        if not self.flag:
            try:
                self._sock.connect((self.domain, self.port))
                self.logger.info('TCPClient connect to {0}:{1} success.'.format(self.domain, self.port))
                self.flag = 1
            except socket.error as e:
                self.logger.exception(e)

    def send(self, send_string):
        """向服务器端发送send_string，并返回信息，若报错，则返回None"""
        self.connect()

        if self.flag:
            try:
                self._sock.send(send_string)
                self.logger.info('TCPClient send "{0}" to server.'.format(send_string))
            except socket.error as e:
                self.logger.exception(e)

            try:
                # 没搞清楚 raw-unicode-escape, unicode-escape 区别
                rec = self._sock.recv(10240).decode('raw-unicode-escape').encode('utf-8')
                self.logger.info('TCPClient get "{0}" from server.'.format(rec))
                return rec
            except socket.error as e:
                self.logger.exception(e)

    def close(self):
        """关闭连接"""
        if self.flag:
            self._sock.close()
            self.logger.info('TCPClient closed.')


if __name__ == '__main__':
    boce = TCPClient('192.168.6.63', 10001)
    r = boce.send('[{"action": "query_spot_commodity_by_id", "data": {"commodity_id":"BRCM"}}]')
    print r
    boce.close()
