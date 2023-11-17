import datetime
from .connection import ConnectionContext, requires_connection, node_id_to_int
from ._aura_pybind import AuraSerialHub, get_version, version_matches_filter
from . import flashage

no_timeout = datetime.timedelta(0)


class AuraHub(ConnectionContext):
    """
    an AuraHub instance manages a connection to the Aura gateway.

    typical usage:
        1. procedural approach
            aura = AuraHub(port_name='...')
            aura.connect()
            ...
            aura.disconnect()

        2. use the client as a context for automatic connection / disconnection:
        with AuraHub() as client:
            ...
    """
    console_prompt = 'aura gw'

    def __init__(self,
                 port_name: str,
                 verbose: bool = False):
        """
        :param port_name: name of a specific port to connect to e.g. COM3 on Windows.
                        if left empty, can be auto-detected.
        """
        self._impl = AuraSerialHub(port_name)
        self._impl.set_verbose(verbose)

    @classmethod
    def get_client_version(cls):
        """
        :return: aura client version
        """
        return get_version()

    def get_port_name(self):
        """
        :return: the serial port name used to connect to the gateway
        """
        return self._impl.get_port_name()

    def connect(self):
        """
        establishes a serial connection to an Aura Gateway
        :return: True on connection success
        """
        return self._impl.connect()

    def disconnect(self, force_disconnect: bool = False):
        """
        disconnects from Aura gateway
        """
        self._impl.disconnect(force_disconnect)

    def is_connected(self):
        return hasattr(self, '_impl') and self._impl.is_connected()

    def has_direct_aura_mc_connection(self):
        return self._impl.has_direct_aura_mc_connection()

    def push_name(self, name: str):
        """
        Changes the gateway name
        :param name: new gateway name
        :return: True on success
        """
        return self._impl.push_name(name)

    def pull_name(self):
        """
        pulls the gateway name
        :return: the gateway name
        """
        return self._impl.pull_name()

    @requires_connection
    def pull_aura_version(self):
        """
        :return: aura firmware version information (i.e. what's running on the actuator)
        """
        return self._impl.pull_aura_version()

    def get_connected_version(self):
        return self._impl.get_connected_version()

    @requires_connection
    def scan_aura_can(self, with_name: bool = True, with_version: bool = True):
        return self._impl.scan_aura_can(with_name=with_name,
                                        with_version=with_version)

    @requires_connection
    def pull_can_id(self):
        return node_id_to_int(self._impl.pull_can_id())

    @requires_connection
    def push_can_id(self, id:int):
        return self._impl.push_can_id(id)

    @requires_connection
    def reboot(self):
        """ reboots the actuator """
        self._impl.reboot()

    @requires_connection
    def start_heartbeat(self):
        """
        starts a regular stream of keep-alive messages
        as a safety measure: the actuator stops unless it receives
        those messages at regular intervals
        """
        self._impl.start_heartbeat()

    @requires_connection
    def stop_heartbeat(self):
        """
        stops stream of keep-alive messages.
        This will cause the actuators to stop after a short while.
        """
        self._impl.stop_heartbeat()

    @requires_connection
    def has_heartbeat(self):
        """
        :return: whether keep-alive messages are being streamed
        """
        return self._impl.has_heartbeat()

    @requires_connection
    def stop(self):
        """
        """
        self.stop_heartbeat()

    @requires_connection
    def send_ascii_command(self, *args, timeout=no_timeout):
        """
        :param args:
        :param timeout: time to wait for reply, in seconds
        :return: command reply (lines of text)
        """
        return self._impl.send_ascii_command(' '.join(args), timeout)

    def impl(self):
        """
        DO NOT USE - not part of the public API
        """
        return self._impl

    def upgrade_firmware(self,
                         version_filter: str = None,
                         update_source: str = flashage.BINARIES_DIR_PATH,
                         interactive: bool = False,
                         update_app: bool = False,
                         update_bootloader: bool = False):

        min_working_version = '>=2023.2.0'
        app_info = self._impl.get_connected_app_info()
        version = app_info.app_version()

        if not version_matches_filter(version, min_working_version):
            print(f"Gateway update requires version {min_working_version}+ (current: {version}).")
            return False

        return flashage.update_aura(self,
                                    version_filter=version_filter,
                                    update_source=update_source,
                                    interactive=interactive,
                                    update_app=update_app,
                                    update_bootloader=update_bootloader)
