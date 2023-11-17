from .auraclient import AuraClient
from .aurahub import AuraHub
from .connection import AuraConnectionError
from .units import *
from . import console
run = console.run_console_loop


def format_cpp_error_message(error_msg):
    """
    Make error message user-friendly by stripping out cpp trace info
    :param error_msg:
    :return: user-friendly error msg
    """
    return error_msg.split('thrown from')[-1].split('\n', 1)[-1]


def get_version():
    """
    :return: aura client version
    """
    from ._aura_pybind import AuraClientCpp
    return AuraClientCpp.get_client_version()


