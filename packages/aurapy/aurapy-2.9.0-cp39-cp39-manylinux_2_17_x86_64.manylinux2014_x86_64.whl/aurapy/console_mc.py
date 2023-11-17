from .console_common import validate_num_args, print_answer, parse_apply
from .dialog_utils import prompt_user_yes_no
from .units import *
from .auraclient import AuraClient
import os
import time


def print_usage():
    print("""
usage:
    st[o]p        -> stops the actuator
    [st]ate       -> fetches actuator state
    [d]uty 0.2    -> sets pwm to 20%
    [s]peed 100   -> sets speed to 100 rpm
    [s]peed_[pid] -> gets/sets the pid parameters when using speed control
    [p]osition 65 -> sets position target to a 65 degrees angle
    [p]os_[pid]   -> gets/sets the pid parameters when using position control
    [c]urrent 1.5 -> sets current target to 1.5 ampere
    [w]ait 1.5    -> sleeps 1.5 second (useful for chaining commands)
    reboot        -> reboot the actuator
    [heart]beat   -> heartbeat:
                    - heart  : fetches heartbeat status
                    - heart 1: starts heartbeat 
                    - heart 0: stops heartbeat
    [sel]ect      -> in the case several devices are connected, selects a different one.   
                    - no argument: prompts user
                    - [port_name][:can_id]: switches to a specific port/CAN id device.
                      Ex: "sel /dev/ttyACM0:2" or "sel COM0:2". 
    version       -> shows client and actuator version
    save          -> persists any temporary changes to the actuator configuration
    [h]elp        -> prints usage

* Numerical parameters support range syntax: start:end:increment:wait_time
    example: 
        speed 100:300:10:0.5 # sets speed from 100 to 300 rpm in increments of 10rpm every 0.5 seconds 
                
* Chain command using ';' as a separator e.g.: speed 100; wait 1; speed 300    
* Press <enter> to repeat the previous command.

Any invalid command will stop the actuator.
    """)


is_verbose = False


def parse_command(client: AuraClient, command, *args):
    """
    Interpret a command string and its arguments to call the
    corresponding method on an AuraClient instance.

    :param client: AuraClient instance to apply the command to
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

    elif command in ('st', 'state'):
        validate_num_args(command, 0, *args)
        print_answer(client.pull_state())

    elif command in ('s', 'speed'):
        if len(args) > 0:
            validate_num_args(command, 1, *args)
            parse_apply(client.command_speed, args[0], rpm)
        else:
            print_answer(client.pull_state().speed)

    elif command in ('c', 'current'):
        if len(args) > 0:
            validate_num_args(command, 1, *args)
            parse_apply(client.command_current, args[0], ampere)
        else:
            print_answer(client.pull_state().current)

    elif command in ('b', 'brake'):
        if len(args) > 0:
            validate_num_args(command, 1, *args)
            parse_apply(client.command_brake_current, args[0], ampere)
        else:
            print_answer(client.pull_state().current)

    elif command in ('p', 'position'):
        if len(args) > 0:
            validate_num_args(command, 1, *args)
            parse_apply(client.command_position, args[0], degree)
        else:
            print_answer(client.pull_state().position)

    elif command in ('clear_config',):
        if prompt_user_yes_no("are you sure?", default_yes=False):
            if client.impl().clear_configuration():
                print("configuration cleared")

    elif command in ('t', 'torque'):
        if len(args) > 0:
            validate_num_args(command, 1, *args)
            # TODO: incomplete feature
            parse_apply(client.impl().command_torque, args[0], newton_meter)
        else:
            # TODO: return torque, not current
            print_answer(client.pull_state().current)

    elif command in ('d', 'duty'):
        if len(args) > 0:
            validate_num_args(command, 1, *args)
            parse_apply(client.command_dutycycle, args[0], dutycycle)
        else:
            print_answer(client.pull_state().dutycycle)

    elif command in ('version',):
        validate_num_args(command, 0, *args)
        print_answer('Aura client  :', client.get_client_version())
        print_answer('Aura actuator:', client.get_connected_version())
        aura_hub = client.impl().get_aura_hub()
        try:
            if not aura_hub.has_direct_aura_mc_connection():
                print_answer('Aura gateway :', aura_hub.get_connected_version())
        except:
            # guarding against legacy (pre aura_mc 2.1.5) UTF-8 conversion error when returning non-ascii UUID
            pass

    elif command in ('calib_icmu',):
        if len(args) == 0:
            client.calibrate_icmu_encoder()
        elif len(args) == 1:
            client.calibrate_icmu_encoder(num_rotations=float(args[0]))
        else:
            validate_num_args(command, 2, *args)
            client.calibrate_icmu_encoder(num_rotations=float(args[0]), debug=bool(args[2]))

    elif command in ('save',):
        validate_num_args(command, 0, *args)
        if client.persist_aura_local_configuration():
            print_answer("Configuration successfully saved")
        else:
            print_answer("An error occurred, the configuration was not saved")

    elif command in ('spid', 'speed_pid'):
        if len(args) > 0:
            validate_num_args(command, 3, *args)
            if not client.push_speed_pid(float(args[0]), float(args[1]), float(args[2])):
                print_answer("An error occurred")
        else:
            for i in zip(("KP: ", "KI: ", "KD: "), client.pull_speed_pid()):
                print(*i)

    elif command in ('ppid', 'pos_pid'):
        if len(args) > 0:
            validate_num_args(command, 3, *args)
            if not client.push_position_pid(float(args[0]), float(args[1]), float(args[2])):
                print_answer("An error occurred")
        else:
            for i in zip(("KP: ", "KI: ", "KD: "), client.pull_position_pid()):
                print(*i)

    elif command in ('h', 'help', 'doc'):
        validate_num_args(command, 0, *args)
        print_usage()

    else:
        return False  # command not found

    return True
