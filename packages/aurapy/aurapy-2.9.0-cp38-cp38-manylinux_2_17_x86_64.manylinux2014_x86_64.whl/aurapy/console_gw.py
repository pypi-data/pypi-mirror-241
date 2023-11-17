from .console_common import validate_num_args, print_answer
from .connection import IOException, TimeoutException, node_id_to_int
from .aurahub import AuraHub
import os
import time


def print_usage():
    print("""
usage:
    st[o]p        -> stops the heartbeat
    can           -> scans the CAN bus for actuators  
    au[x]         -> auxiliary power: 
                        - aux  : fetches aux power status
                        - aux 1: switches on aux power 
                        - aux 0: switches off aux power                         
    [heart]beat   -> heartbeat:
                        - heart  : fetches heartbeat status
                        - heart 1: starts heartbeat 
                        - heart 0: stops heartbeat
    [w]ait 1.5    -> sleeps 1.5 second (useful for chaining commands)
    reboot        -> reboot the device
    [sel]ect      -> in the case several devices are connected, selects a different one.   
                    - no argument: prompts user
                    - [port_name][:can_id]: switches to a specific port/CAN id device.
                      Ex: "sel /dev/ttyACM0:2" or "sel COM0:2". 
    version       -> shows client and device version    
    [h]elp        -> prints usage

* Press <enter> to repeat the previous command.
    """)


is_verbose = False


def parse_command(client: AuraHub, command: str, *args):
    """
    Interpret a command string and its arguments to call the
    corresponding method on an AuraHub instance.

    :param client: AuraHub instance to apply the command to
    :param command: a string representing a command line input.
    :param args: optional command arguments as string.
    :return: True if command was valid
    """

    global is_verbose

    if command == 'verbose':
        validate_num_args(command, 0, *args)
        is_verbose = not is_verbose
        client.impl().set_verbose(is_verbose)

    elif command == 'noverbose':
        validate_num_args(command, 0, *args)
        is_verbose = False

    elif command in ('can', 'scan', 'bus'):
        scan = client.scan_aura_can(with_name=True, with_version=True)
        if len(scan) == 0:
            print('no actuator found on CAN bus')
        else:
            for item in scan:
                print(node_id_to_int(item.id),
                      item.name,
                      item.version.app_full(),
                      item.version.compile_timestamp())

    elif command in ('version',):
        validate_num_args(command, 0, *args)
        print_answer('Aura client :', client.get_client_version())
        print_answer('Aura gateway:', client.get_connected_version())

    elif command in ('h', 'help', 'doc'):
        validate_num_args(command, 0, *args)
        print_usage()

    elif command in ('x', 'aux'):
        if len(args) > 0:
            validate_num_args(command, 1, *args)
            reply = client.send_ascii_command('auxiliary_power', args[0], timeout=1)
        else:
            reply = client.send_ascii_command('auxiliary_power', timeout=1)
        for line in reply:
            print(line)

    else:
        return False

    return True
