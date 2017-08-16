import struct
_GLOBAL_DEFAULT_TIMEOUT = 0
AF_INET = 0
SOCK_STREAM = 0
SOCK_DGRAM = 0


def gethostname():
    return "mock_hostname"


class socket(object):
    def __init__(self, inet, stream):
        self.last_send = ""
        self.close_called = False

    def connect(self, connection):
        pass

    def recv(self, bytes):
        return "Test\n> "

    def send(self, data):
        self.last_send = data

    def close(self):
        self.close_called = True
