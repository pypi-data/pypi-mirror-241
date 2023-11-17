import time
import os

from ._aura_pybind import select_binaries, version_matches_filter, print_aura_version, TimeoutException, BootKey
from .dialog_utils import prompt_user_yes_no


BINARIES_DIR_NAME = 'binaries'
BINARIES_DIR_PATH = os.path.join(os.path.dirname(__file__), BINARIES_DIR_NAME)

NO_VERSION_FILTER = ''
BUNDLED_BINARY = 'bundled'  # versions present in the update binary on the board
PACKAGED_BINARIES = 'packaged'  # versions included in the aurapy python package


def get_binary_full_path(directory: str, binary_file_name: str):
    if os.path.exists(binary_file_name):
        return binary_file_name
    else:
        path = os.path.join(directory, binary_file_name)
        if not os.path.exists(path):
            raise ValueError(f"path not found: {path}")
        return path


def select_binary(client, version_filter: str = None, path: str = BINARIES_DIR_PATH, choose: bool = None):
    path = os.getcwd() if not path else path

    current_version = client.get_connected_version()

    upgrade = version_filter is None
    if upgrade:
        version_filter = "> " + current_version.split('-')[1]

    verbose = True
    candidate_bins = select_binaries(current_version, version_filter, path, verbose)

    print_version(client, "current version:")

    if len(candidate_bins) > 1 and (choose is None or choose):
        print(f"Available update" + ("s" if len(candidate_bins) > 1 else "") + ":")
        for i in range(len(candidate_bins)):
            version = candidate_bins[i].split("-")[1]
            print(f'     {i}: {candidate_bins[i]} ({version})')

        try:
            i = int(input("select an update to perform, anything else to abort: "))
            return get_binary_full_path(path, candidate_bins[i])
        except IndexError:
            return ''
        except ValueError:
            return ''
        except KeyboardInterrupt:
            return ''

    elif candidate_bins:
        if choose:
            print("found one suitable binary:")
            print(f'      : {candidate_bins[0]}')
            try:
                if not prompt_user_yes_no("proceed with the update?"):
                    return ''
            except KeyboardInterrupt:
                return ''
        if os.path.isdir(path):
            return get_binary_full_path(path, candidate_bins[-1])
        else:
            return path

    else:
        raise Exception(f"no binary candidate found" + f"(filter: {version_filter})" if version_filter else "")


def check_app_version_compatibility(client, update_source, update_bootloader):
    min_working_version = '>=2023.2.9'
    app_info = client.impl().get_connected_app_info()
    version = app_info.app_version()
    if update_bootloader or update_source in [BUNDLED_BINARY, None]:
        if not version_matches_filter(version, min_working_version):
            print(f"Bundle or Bootloader update requires version {min_working_version}+ (current: {version})."
                  f" Update the application first.")
            return False

    return True


def update_aura(client,
                version_filter: str = NO_VERSION_FILTER,
                update_source: str = None,
                interactive: bool = None,
                update_app: bool = False,
                update_bootloader: bool = False
                ):
    success = False

    update_from_bundle = update_source == BUNDLED_BINARY
    if update_bootloader or update_from_bundle:
        if not check_app_version_compatibility(client, update_source, update_bootloader=update_bootloader):
            return False

    if update_from_bundle:
        assert version_filter == NO_VERSION_FILTER, "version filter cannot be specified for a bundled binary"
        go_ahead = True

        if interactive:
            update_targets = []
            if update_app:
                update_targets.append('app')
            if update_bootloader:
                update_targets.append('booloader')
            if update_targets:
                go_ahead = prompt_user_yes_no(f"Update {', '.join(update_targets)} from on-board binary version?",
                                              default_yes=True)
            else:
                print(' no upload or install needed')
                return False  # Nothing to do

        if go_ahead:
            success = client.impl().update_firmware('', update_app, update_bootloader, True)
        else:
            return False
    else:
        path = update_source
        if path == PACKAGED_BINARIES:
            path = BINARIES_DIR_PATH

        filename = select_binary(client=client,
                                 version_filter=version_filter,
                                 path=path,
                                 choose=interactive)

        if filename:
            print("")
            if interactive and update_app is None:
                update_app = prompt_user_yes_no("Install the new software after upload and reboot aura?",
                                                default_yes=False)
            success = client.impl().update_firmware(filename,
                                                    update_app,
                                                    update_bootloader,
                                                    True)

    return success


def print_version(client, prefix="version:"):
    current_version = client.get_connected_version()
    print(prefix)
    print_aura_version(current_version)


def poll_new_version(client):
    sleep_delay_sec = 2
    waited_so_far_sec = 0

    while not client.connect(silent=True):
        if waited_so_far_sec > 10:
            print("The board does not respond, check if it is still properly connected")
            print("If so you can try to power cycle it")
            return False
        time.sleep(sleep_delay_sec)
        waited_so_far_sec += sleep_delay_sec

    print_version(client, "new version successfully installed:")
    return True
