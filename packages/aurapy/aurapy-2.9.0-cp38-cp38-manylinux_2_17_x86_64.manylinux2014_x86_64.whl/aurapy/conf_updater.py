#!/usr/bin/python3
import os
import sys

aurapy_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(aurapy_path)
import aurapy
import argparse
from aurapy import _aura_pybind as aura

python_exe = os.path.basename(sys.executable)

parser = argparse.ArgumentParser(
    prog=f'{python_exe} -m {__name__}',
    description="{__name__} options",
    formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument("arg",
                    help="either an aura model name to get the default config for, or a path to a config file")
parser.add_argument("name",
                    nargs="?",
                    default="<no_name>",
                    help="a user-friendly name to store in the config - helps identify a particular aura instance")
parser.add_argument("--no-clear",
                    action='store_true',
                    help="default is to clear the flash memory of preceding config data before writing the new one,"
                         " instead of just appending the new config to existing flash memory contents")
parser.add_argument("--no-write",
                    action='store_true',
                    help="This flag specifies that the config should only be "
                         "set in RAM, not persisted to flash.")


def update_conf(conf_arg, name=None, clear_existing_config=True, persist_config=True):
    """
    Utility function to Write configuration data to an Aura board.

    :param conf_arg: this param can be either:
        - an instance of a configuration,
        - the name of an aura model e.g. AURA_M_450
        - a path to a file containing configuration data
    :param name: optional user-friendly name in 32 characters to write to the config
    :param clear_existing_config: whether to erase the flash sector
    :param persist_config: whether the config is persisted on the aura board (writen to flash) or just set in RAM.
    :return:
    """
    if isinstance(conf_arg, aura.aura_mc_conf_t):
        conf = conf_arg
        if name is not None:
            conf.aura_name = aura.string_to_aura_name(name)
    elif hasattr(aura.AuraModel, conf_arg):
        aura_model = getattr(aura.AuraModel, conf_arg)
        print(f"updating conf for {aura_model} with name '{name}'")
        conf = aura.get_default_configuration(aura_model=aura_model, name=name if name is not None else '')
    elif os.path.isfile(conf_arg):
        conf = aura.load_configuration_from_file(conf_arg)
        if name is not None:
            conf.aura_name = aura.string_to_aura_name(name)
            print('aura_name', ''.join(conf.aura_name))
    else:
        print()
        raise ValueError(f"{conf_arg} is neither an aura model nor a path to a config file")

    with aurapy.AuraClient() as client:
        if clear_existing_config:
            print('clearing existing confg')
            client._aura_client_impl.clear_configuration()
        client._aura_client_impl.push_configuration(conf, store_it=persist_config)


if __name__ == '__main__':
    args = parser.parse_args()
    try:
        update_conf(args.arg,
                    name=args.name,
                    clear_existing_config=not args.no_clear,
                    persist_config=not args.no_write)
    except ValueError as exc:
        print(exc)
    except Exception as exc:
        pass

