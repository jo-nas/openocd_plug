import sys
import pytest
import mock_socket
sys.modules['socket'] = mock_socket

import openocd_plug


@pytest.fixture
def ocd_plug():
    return openocd_plug.OpenOCDPlug()


def test_it_can_create_an_instance(ocd_plug):
    assert isinstance(ocd_plug, openocd_plug.OpenOCDPlug)


def test_it_can_create_a_connection(ocd_plug):
    assert ocd_plug.port == 4444
    assert ocd_plug.ip == "127.0.0.1"
    assert isinstance(ocd_plug.sock, mock_socket.socket)


def test_it_can_send_a_reset(ocd_plug):
    ocd_plug.reset()
    assert ocd_plug.sock.last_send == "reset\n"


def test_it_can_send_a_reset_run(ocd_plug):
    ocd_plug.reset_run()
    assert ocd_plug.sock.last_send == "reset run\n"


def test_it_can_send_a_reset_halt(ocd_plug):
    ocd_plug.reset_halt()
    assert ocd_plug.sock.last_send == "reset halt\n"


def test_it_can_send_a_reset_init(ocd_plug):
    ocd_plug.reset_init()
    assert ocd_plug.sock.last_send == "reset init\n"


def test_it_can_send_a_exit(ocd_plug):
    ocd_plug.exit()
    assert ocd_plug.sock.last_send == "exit\n"


def test_it_can_send_the_debug_level(ocd_plug):
    for i in range(-3, 3):
        ocd_plug.debug_level(i)
        assert ocd_plug.sock.last_send == "debug_level {}\n".format(i)


def test_it_can_send_a_halt(ocd_plug):
    ocd_plug.halt()
    assert ocd_plug.sock.last_send == "halt\n"


def test_it_can_send_a_halt_with_delay(ocd_plug):
    ocd_plug.halt(10000)
    assert ocd_plug.sock.last_send == "halt 10000\n"


def test_it_can_send_a_program_firmware_command(ocd_plug):
    ocd_plug.program("TEST.hex")
    assert ocd_plug.sock.last_send == "program TEST.hex  verify reset\n"


def test_it_can_send_a_program_firmware_command(ocd_plug):
    ocd_plug.program("TEST.hex")
    assert ocd_plug.sock.last_send == "program TEST.hex  verify reset\n"


def test_it_can_send_a_program_firmware_command_without_reset(ocd_plug):
    ocd_plug.program("TEST.hex", reset=False)
    assert ocd_plug.sock.last_send == "program TEST.hex  verify \n"


def test_it_can_send_a_program_firmware_command_without_verify(ocd_plug):
    ocd_plug.program("TEST.hex", verify=False)
    assert ocd_plug.sock.last_send == "program TEST.hex   reset\n"


def test_it_can_send_a_program_firmware_command_without_verify_and_reset(ocd_plug):
    ocd_plug.program("TEST.hex", reset=False, verify=False)
    assert ocd_plug.sock.last_send == "program TEST.hex   \n"


def test_it_can_send_a_program_firmware_command_with_data_address(ocd_plug):
    ocd_plug.program("TEST.hex", 0x800000)
    assert ocd_plug.sock.last_send == "program TEST.hex 0x800000 verify reset\n"


def test_it_can_teardown_itself(ocd_plug):
    ocd_plug.tearDown()
    assert ocd_plug.sock.last_send == "exit\n"
    assert ocd_plug.sock.close_called is True
