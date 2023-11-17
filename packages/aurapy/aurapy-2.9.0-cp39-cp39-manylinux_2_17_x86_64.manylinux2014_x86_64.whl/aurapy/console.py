"""
 console: a command-line interface for driving aura actuator.
"""
from . import selector
import time
from .connection import TimeoutException, AuraConnectionError, print_exc
from .console_common import InvalidCommand, SelectClientException, validate_num_args, print_answer
from . import console_mc, console_gw
import sys
from . import AuraClient


def print_basic_usage():
    print("""Aura command line tool.
    press <CTRL> + C twice to exit.
    type help for usage.""")


def parse_command(client, command, *args):
    try:
        _parse_command(client, command, *args)
    except (InvalidCommand, SelectClientException):
        raise
    except Exception as exc:
        raise InvalidCommand(str(exc))


def _parse_command(client, command, *args):

    if command in ('sel', 'select'):
        port_hint = device_hint = None
        if len(args) > 0:
            if len(args) > 1:
                raise InvalidCommand('expects a single argument in the format: port_name:device_id')
            port_hint, device_hint = parse_selection_hints(args[0])
            if port_hint is None:
                port_hint = client.get_port_name()
        raise SelectClientException(port_hint=port_hint,
                                    device_hint=device_hint)

    elif command == 'exit':
        validate_num_args(command, 0, *args)
        return True  # exit requested

    elif command in ('o', 'stop'):
        validate_num_args(command, 0, *args)
        client.stop()

    elif command in ('reboot',):
        client.reboot()

    elif command in ('w', 'wait'):
        validate_num_args(command, 1, *args)
        val = float(args[0])
        time.sleep(val)

    elif command in ('heart', 'heartbeat'):
        if len(args) > 0:
            validate_num_args(command, 1, *args)
            if int(args[0]):
                client.start_heartbeat()
            else:
                client.stop_heartbeat()
        else:
            print_answer('heartbeat is', 'on' if client.has_heartbeat() else 'off')

    elif command.startswith('a'):
        # everything after the '_' is interpreted as an ascii command
        try:
            reply = client.impl().send_ascii_command(' '.join(args), 1)
            for line in reply:
                print(line)
        except TimeoutException:
            pass

    elif command.startswith('_'):
        # everything after the '_' is interpreted by the pybind client
        try:
            reply = getattr(client.impl(), command[1:])(*[eval(a) for a in args])
            print(reply)
        except TimeoutException:
            pass

    else:

        if isinstance(client, AuraClient):
            success = console_mc.parse_command(client, command, *args)
        else:
            success = console_gw.parse_command(client, command, *args)

        if not success:
            raise InvalidCommand(f"invalid command: {command} {' '.join(args)}")


def process_command_line(client, command_line_str):
    """
    Processes a command line input.
    :param client: AuraClient instance
    :param command_line_str: one or many ';' separated commands
    :return:
    """
    commands = command_line_str.split(';')

    for command_str in commands:
        command_str = command_str.strip()
        if command_str:
            exit_requested = parse_command(client, *command_str.split())
            if exit_requested:
                return True

    return False


def _run_console_loop(initial_command=None, no_loop=False, port_hint=None, device_hint=None):
    """
    The main loop of the command line interface

    :param initial_command: an optional command to run at startup.
    """
    input_str = initial_command
    armed_exit = False

    with selector.select_client(port_hint=port_hint,
                                device_hint=device_hint) as client:

        name = client.pull_name()
        print(f'Connected to {name if len(name) else "<no name>"} '
              f'on serial port: {client.get_port_name()}')
        print()
        if not no_loop:
            print_basic_usage()
            print()

        command_line_str = input_str
        while client.is_connected():
            try:
                if command_line_str is not None:
                    armed_exit = False
                    try:
                        exit_requested = process_command_line(client, command_line_str)
                        if exit_requested:
                            break

                    except InvalidCommand as exc:
                        client.stop()
                        print(exc)
                        print('stopping')

                if no_loop:
                    return

                input_str = input(client.console_prompt + '>> ')

                if input_str:
                    command_line_str = input_str
                armed_exit = False

            except KeyboardInterrupt:
                if sys.platform.startswith('linux'):
                    print("")
                if armed_exit:
                    try:
                        input_str = input('\nDo you really want to exit aura cli ([y]/n)?')
                    except KeyboardInterrupt:
                        if sys.platform.startswith('linux'):
                            print("")
                        input_str = 'y'

                    input_str = input_str.strip()
                    if not input_str or input_str.lower() == 'y':
                        break
                    else:
                        armed_exit = False
                        continue

                command_line_str = None
                armed_exit = True
                client.stop()
                print()


def parse_selection_hints(arg: str):

    if ':' in arg:
        port_hint, device_hint = arg.split(':', 1)
    else:
        port_hint = arg
        device_hint = None

    if port_hint == '':
        port_hint = None
    if device_hint == '':
        device_hint = None

    return port_hint, device_hint


def run_console_loop(initial_command=None, no_loop=False, port_hint=None, device_hint=None):
    """
    The main loop of the command line interface

    :param initial_command: an optional command to run at startup.
    :param no_loop: exit right away (e.g. after executing initial command)
    :param port_hint:
    :param device_hint:
    """
    in_client_selection_mode = False
    while True:
        try:
            return _run_console_loop(initial_command=initial_command,
                                     no_loop=no_loop,
                                     port_hint=port_hint,
                                     device_hint=device_hint)
        except SelectClientException as exc:
            initial_command = None
            port_hint = exc.port_hint
            device_hint = exc.device_hint
            in_client_selection_mode = True

        except AuraConnectionError as exc:
            print_exc(exc)
            print()
            if not in_client_selection_mode:
                break
            port_hint = device_hint = None

        except Exception as exc:
            print_exc(exc)
            break
