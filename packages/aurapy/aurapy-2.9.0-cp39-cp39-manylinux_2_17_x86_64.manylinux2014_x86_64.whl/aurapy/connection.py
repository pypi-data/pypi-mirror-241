import sys
from functools import wraps
from ._aura_pybind import IOException, TimeoutException, AuraSerialHub
from typing import Union

def print_exc(exc, comment=""):
    print(str(exc) + comment, end="\n", file=sys.stderr)


def available_ports():
    return AuraSerialHub.list_aura_ports()


def print_port(port):
    print('           name:', port.name)
    print('    description:', port.description)
    print('         device:', port.hardware_id)


def node_id_to_int(i):
    return int.from_bytes(i, "big")


class AuraConnectionError(BaseException):
    pass


def select_port(port_hint: Union[str, int] = None, verbose: bool = False) -> str:
    """
    Select a serial port available for connection.
    :param port_hint: if several actuators are present,
           whether to prompt user to select one or just return the first one.
    :param verbose:
    :return: selected port name or empty string if no selection
    """
    serial_ports = available_ports()

    if not serial_ports:
        return ''

    if port_hint is not None:
        if isinstance(port_hint, int):
            num_ports = len(serial_ports)
            if port_hint >= num_ports or port_hint < 0 and abs(port_hint) - 1 > num_ports:
                if verbose:
                    print(f'invalid port index: {port_hint} - {len(serial_ports)} ports found')
                return ''
            return serial_ports[port_hint].name
        else:
            for port_info in serial_ports:
                if port_info.name == port_hint:
                    return port_info.name

        if verbose:
            print(f'invalid port choice: {port_hint}')
        return ''

    port_index = 0

    if len(serial_ports) > 1:
        # Choice is obvious if there is a single option

        default_index = None
        for i, port in enumerate(serial_ports):
            print_port(port)
            print()

        if default_index is not None:
            port_index = default_index

        while True:
            print("Available serial ports:")
            print(f'     {0}: {"Auto-detect"}')
            for i, port in enumerate(serial_ports):
                print(f'     {i + 1}: {port.description}')

            port_index_input = input(f'select port to connect to [default: {port_index + 1}]\n')
            if port_index_input:
                port_index = int(port_index_input) - 1
                if port_index < -1 or port_index >= len(serial_ports):
                    print(f'invalid selection: {port_index_input} - try again')
                    print()
                    continue

            break

    if port_index == -1:
        return ''

    return serial_ports[port_index].name


def exception_handler(func, exception_types, message):
    """
    Decorator for handling exceptions, e.g. make message more user-friendly
    by avoiding long stack trace in favor of concise message.
    :param func:
    :param exception_types: exception type to filter for or a tuple of several such exception types
    :param message: message to print when catching an exception of type exception_type
    :return: decorated function.
    """

    @wraps(func)
    def wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except exception_types:
            print(message)

    return wrapped


def requires_connection(func):
    """
    Decorator for functions which require to be connected
    :param func: function to be decorated
    :return: decorated function.
    """
    return exception_handler(
        func,
        AuraConnectionError,
        "not connected - please connect first by calling .connect()")


class ConnectionContext:

    def connect(self):
        raise NotImplementedError

    def disconnect(self):
        raise NotImplementedError

    def is_connected(self):
        raise NotImplementedError

    def __enter__(self):
        if not self.connect():
            raise Exception("Connection attempt failed")
        return self

    def __exit__(self, type, value, traceback):
        if self.is_connected():
            self.disconnect()

    def __del__(self):
        # disconnect on object destruction
        if self.is_connected():
            self.disconnect()
