import socket
from openhtf import plugs
from openhtf import conf

conf.declare(
    'openocd_ip',
    default_value="127.0.0.1",
    description='The IP-Address for the OpenOCD device.'
)

conf.declare(
    'openocd_port',
    default_value=4444,
    description='The telnet port to OpenOCD.'
)


class OpenOCDPlug(plugs.BasePlug):
    @conf.inject_positional_args
    def __init__(self, openocd_ip, openocd_port):
        self.ip = openocd_ip
        self.port = openocd_port

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.ip, self.port))
        except:
            import subprocess
            subprocess.call("cd ~")
            subprocess.call("openocd")
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.ip, self.port))

        self.receive()
        self.debug_level(0)

    def tearDown(self):
        try:
            self.exit()
        finally:
            self.sock.close()

    def query(self, cmd):
        self.send(cmd)
        return self.receive()

    def send(self, cmd):
        self.sock.send((cmd + "\n").encode("ascii"))

    def receive(self):
        """Read from the stream until the token (\x1a) was received."""
        data = bytes()
        while True:
            chunk = self.sock.recv(4096)
            data += chunk
            if "> " in chunk:
                break

        return data.replace("> ", "").split("\n", 1)[1]

    def reset(self):
        return self.query("reset")

    def reset_run(self):
        return self.query("reset run")

    def reset_halt(self):
        return self.query("reset halt")

    def reset_init(self):
        return self.query("reset init")

    def exit(self):
        return self.query("exit")

    def debug_level(self, level):
        return self.query("debug_level {}".format(level))

    def halt(self, milli_seconds=None):
        return self.query("halt {}".format(milli_seconds) if milli_seconds else "halt")

    def program(self, filename, address=None, verify=True, reset=True):
        return self.query("program {filename} {address} {verify} {reset}".format(
            filename=filename,
            address='0x{:02X}'.format(address) if address else "",
            verify="verify" if verify else "",
            reset="reset" if reset else "",
        ))
