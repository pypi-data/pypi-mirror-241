import datetime
from .connection import select_port, ConnectionContext, requires_connection, print_exc, node_id_to_int, AuraConnectionError
from . import flashage
from ._aura_pybind import AuraClientCpp, AuraSerialHub
from ._aura_pybind import TimeoutException, IOException
from .dialog_utils import prompt_user_yes_no, requires_aura_version
from .units import *
from .units import hertz, seconds, dutycycles, amperes, volts, revolutions_per_minute
from .aurahub import AuraHub
import sys
from typing import Union

no_timeout = datetime.timedelta(0)


class AuraClient(ConnectionContext):
    """
    an AuraClient instance manages a connection to the Aura actuator.

    typical usage:
        1. procedural approach
            aura = AuraClient()
            aura.connect()
            aura.command_dutycycle(0.15)
            time.sleep(10)
            aura.disconnect()

        2. use the client as a context for automatic connection / disconnection:
        with AuraClient() as aura:
            aura.command_dutycycle(0.15)
            time.sleep(10)
    """

    console_prompt = 'aura'

    def __init__(self,
                 port_name: str = "",
                 aura_hub: AuraHub = None,
                 aura_id: int = None,
                 verbose: bool = False,
                 device_hint: Union[str, int] = None):
        """
        :param port_name: name of a specific port to connect to e.g. COM3 on Windows.
                        if left empty, can be auto-detected.
        :param aura_hub, aura_id: advanced parameters - leave at default
        :param device_hint : if several actuators are present, whether to prompt user to select one (if not, select the first one)
        """
        if aura_id is not None:
            if aura_hub is None:
                self._aura_client_impl = AuraClientCpp(aura_id)
            else:
                self._aura_client_impl = AuraClientCpp(aura_hub._impl, aura_id)
        else:
            if aura_hub is None:
                self._aura_client_impl = AuraClientCpp()
            else:
                self._aura_client_impl = AuraClientCpp(aura_hub._impl)

        self.device_hint = device_hint

        if len(port_name):
            if aura_hub is None or aura_hub.get_port_name() != port_name:
                self._aura_client_impl.get_aura_hub().set_port_name(port_name)

        self._aura_client_impl.set_verbose(verbose)

        self.run_checks_on_disconnect = True

    def push_name(self, name: str, persistent: bool = True):
        """
        Changes the actuator name
        :param name: new actuator name
        :param persistent: whether the new name should persist across a reboot
        :return: True on success
        """
        return self._aura_client_impl.push_name(name, persistent)

    def pull_name(self):
        """
        pulls the actuator name
        :return: the actuator name
        """
        return self._aura_client_impl.pull_name()

    def get_name(self):
        """
        gets the actuator name known on the client side (no communication with the actuator)
        :return: the actuator name
        """
        return self._aura_client_impl.get_name()

    def get_node_id(self):
        """
        :return: actuator identifier (e.g. on CAN Bus)
        """
        return node_id_to_int(self._aura_client_impl.get_node_id())

    def push_node_id(self, node_id: int):
        """
        :param node_id: new node identifier (e.g. CAN id on a CAN bus)
        :return: True on success
        """
        return self._aura_client_impl.push_node_id(node_id)

    def get_port_name(self):
        """
        :return: the serial port name used to connect to the actuator
        """
        return self._aura_client_impl.get_aura_hub().get_port_name()

    def connect(self, silent: bool = False):
        """
        establishes a serial connection to an Aura actuator
        :return: True on connection success
        """

        if not self.get_port_name():

            port_name = select_port()
            if not port_name:
                if not silent:
                    print(f"No serial ports found - make sure Aura is connected to your computer")
                return False

            # if not silent:
            #     print('Connecting to serial:', port_name)
            self._aura_client_impl.get_aura_hub().set_port_name(port_name)

        try:

            if not self._aura_client_impl.is_aura_id_assigned():
                aura_hub = self._aura_client_impl.get_aura_hub()
                aura_hub.connect()
                if not aura_hub.has_direct_aura_mc_connection():
                    print(f"Connected to Aura gateway on {aura_hub.get_port_name()}")
                    scanned_nodes = aura_hub.scan_aura_can(with_name=True)
                    nodes_by_id = dict((node_id_to_int(node_info.id), node_info) for node_info in scanned_nodes)

                    if len(scanned_nodes) == 0:
                        raise AuraConnectionError("The gateway could not find any Aura actuator - "
                                                  "please double-check actuators are correctly plugged to the bus.")

                    elif self.device_hint is not None:
                        try:
                            device_hint_int = int(self.device_hint)
                        except ValueError:
                            device_hint_int = None

                        for node_id, node_info in nodes_by_id.items():
                            if node_info.name == self.device_hint or node_id == device_hint_int:
                                selected_id = node_id
                                break
                        else:
                            msg = f'No device found for id {self.device_hint}'
                            #msg += f" ({', '.join(str(node_id) for node_id in nodes_by_id)} are available)"
                            raise AuraConnectionError(msg)

                    elif len(scanned_nodes) > 1:
                        print("Available actuators:")
                        while True:

                            for node_id, node_info in nodes_by_id.items():
                                print(f'   {node_id}: {node_info.name}')

                            selected_id = list(nodes_by_id.keys())[0]
                            user_input = input(f'select actuator: [default: {selected_id}]\n')
                            if user_input:
                                selected_id = int(user_input)
                                if selected_id in nodes_by_id:
                                    break
                                else:
                                    print('invalid selection:', selected_id)
                                    print()
                            else:
                                break  # use selection default
                    else:
                        selected_id = list(nodes_by_id.keys())[0]

                    aura_hub.reassign_client_id(self._aura_client_impl.get_node_id(),
                                                nodes_by_id[selected_id].id)

            try:
                self._aura_client_impl.connect()
            except TimeoutException:
                if self._aura_client_impl.is_aura_id_assigned():
                    if not silent:
                        print("no actuator with id", node_id_to_int(self._aura_client_impl.get_node_id()))
                return False

        except (RuntimeError, IOException) as exc:
            if not silent:
                print_exc(exc)
            return False

        return True

    def disconnect(self, force_disconnect: bool = False, silent: bool = False):
        """
        disconnects from Aura actuator
        """
        if not silent and self.run_checks_on_disconnect and self.aura_has_volatile_changes():
            self.print_volatile_changes_warning()

        self._aura_client_impl.disconnect(force_disconnect)

    def print_volatile_changes_warning(self, prompt_save: bool = False):
        print("*** Some changes in the actuator configuration are not stored "
              "in the persistent memory and will be lost upon reboot if you do not save them. ***")

        if prompt_save:
            if prompt_user_yes_no("Do you want to save those changes now?", default_yes=False):
                self.persist_aura_local_configuration()
                print('changes have been persisted.')
                return True
        return False

    @requires_aura_version(">0.1.0")
    def aura_has_volatile_changes(self):
        return self._aura_client_impl.aura_has_volatile_changes()

    def persist_aura_local_configuration(self):
        return self._aura_client_impl.persist_aura_local_configuration()

    def is_connected(self):
        return hasattr(self, '_aura_client_impl') and self._aura_client_impl.is_connected()

    @classmethod
    def get_client_version(cls):
        """
        :return: aura client version
        """
        return AuraClientCpp.get_client_version()

    @requires_connection
    def pull_aura_version(self):
        """
        :return: aura firmware version information (i.e. what's running on the actuator)
        """
        return self._aura_client_impl.pull_aura_version()

    def get_connected_version(self):
        return self._aura_client_impl.get_connected_version()

    @requires_connection
    def command_dutycycle(self, duty: dutycycles, timeout=no_timeout):
        """
        :param duty: 0.10 for 10% - a negative will reverse the rotation direction

        :param timeout:
            if no_timeout, fires and forget,
            else, expects a handshake reply within that time and raises otherwise
        """
        val_duty = dutycycles(duty)
        if abs(val_duty) > dutycycles(1):
            raise ValueError("dutycycle must be a number in [-1, 1]")

        return self._aura_client_impl.command_dutycycle(val_duty, timeout)

    @requires_connection
    def command_speed(self, speed: revolutions_per_minute, timeout=no_timeout):
        """
        :param speed: speed in rpm. A negative number will reverse the rotation direction

        :param timeout:
            if no_timeout, fires and forget,
            else, expects a handshake reply within that time and raises otherwise
        """
        gear_ratio = 1
        speed = rpm(speed) * gear_ratio
        return self._aura_client_impl.command_speed(speed, timeout)

    @requires_connection
    def push_speed_pid(self, kp: float, ki: float, kd: float):
        """
        :param kp: proportional term of the controller
        :param ki: integral term of the controller (in hertz)
        :param kd: derivative term of the controller (in seconds)
        """
        return self._aura_client_impl.push_speed_pid(kp,
                                                     hertz(ki),
                                                     seconds(kd))

    @requires_connection
    def pull_speed_pid(self):
        """
        :return (kp, ki, kd): pid coefficients
        """
        return self._aura_client_impl.pull_speed_pid()

    @requires_connection
    def push_position_pid(self, kp: float, ki: float, kd: float):
        """
        :param kp: proportional term of the controller
        :param ki: integral term of the controller (in hertz)
        :param kd: derivative term of the controller (in seconds)
        """
        return self._aura_client_impl.push_position_pid(kp, hertz(ki), second(kd))

    @requires_connection
    def pull_position_pid(self):
        """
        :return (kp, ki, kd): pid coefficients
        """
        return self._aura_client_impl.pull_position_pid()

    @requires_connection
    def command_position(self, angular_position: degree, timeout=no_timeout):
        """
        :param angular_position: angular_position in degrees. A negative number will reverse the rotation direction

        :param timeout:
            if no_timeout, fires and forget,
            else, expects a handshake reply within that time and raises otherwise
        """
        return self._aura_client_impl.command_position(angular_position, timeout)

    @requires_connection
    def push_multi_turn_position(self, use_multi_turn: bool, store_change: bool = False):
        """
        use multi-turn position or limit position to [0-360[
        :param use_multi_turn:
        :param store_change: whether to persist this setting to flash memory (saved across reboot)
        """
        return self._aura_client_impl.push_multi_turn_position(use_multi_turn, store_change)

    @requires_connection
    def pull_multi_turn_position(self, from_store: bool = False):
        return self._aura_client_impl.pull_multi_turn_position(from_store)

    @requires_connection
    def push_position_zero(self, angular_position: degree, store_change: bool = False):
        """
        Sets a new position zero
        :param angular_position: angular_position in degrees to use as the zero position.
        :param store_change: whether to persist this setting to flash memory (saved across reboot)
        """
        return self._aura_client_impl.push_position_zero(angular_position, store_change)

    @requires_connection
    def reset_position_zero(self, store_change: bool = False):
        """
        resets the position zero to the current position
        :param store_change: whether to persist this setting to flash memory (saved across reboot)
        """
        return self._aura_client_impl.reset_position_zero(store_change)

    @requires_connection
    def command_current(self, current: amperes, timeout=no_timeout):
        """
        :param current: in Amperes
            sets a target motor current (iq). Rotation direction depends on the sign.

        :param timeout:
            if no_timeout, sends the command and forget,
            else, expects a handshake reply within that time and raises otherwise
        """
        return self._aura_client_impl.command_current(amperes(current), timeout)

    @requires_connection
    def command_brake_current(self, current: amperes, timeout=no_timeout):
        """
        :param current: in Amperes
            sets a target brake current (iq). Sign of the value does not matter.

        :param timeout:
            if no_timeout, sends the command and forget,
            else, expects a handshake reply within that time and raises otherwise
        """
        return self._aura_client_impl.command_brake_current(amperes(current), timeout)

    @requires_connection
    def push_max_current(self, current: amperes):
        """
        :param current: maximum current draw in Amperes.
        Provides a way to limit torque.
        """
        return self._aura_client_impl.push_max_current(amperes(current))

    @requires_connection
    def pull_max_current(self):
        """
        :return: configured maximum current draw in Amperes.
        """
        return self._aura_client_impl.pull_max_current()

    '''
    # unavailable pending proper kt measurement
    @requires_connection
    def command_torque(self, torque):
        """
        :param torque: in newton-meter
            the sign of the value determines the direction of movement
        """
        self._aura_client_impl.command_current(torque)
    '''

    @requires_connection
    def start_heartbeat(self):
        """
        starts a regular stream of keep-alive messages
        as a safety measure: the actuator stops unless it receives
        those messages at regular intervals
        """
        self._aura_client_impl.get_aura_hub().start_heartbeat()

    @requires_connection
    def stop_heartbeat(self):
        """
        stops stream of keep-alive messages.
        This will cause the actuator to stop after a short while.
        """
        self._aura_client_impl.get_aura_hub().stop_heartbeat()

    @requires_connection
    def has_heartbeat(self):
        """
        :return: whether keep-alive messages are being streamed
        """
        return self._aura_client_impl.get_aura_hub().has_heartbeat()

    @requires_connection
    def stop(self, timeout=no_timeout):
        """
        stops the Actuator - no brake applied

        :param timeout:
            if no_timeout, fires and forget,
            else, expects a handshake reply within that time and raises otherwise
        """
        return self._aura_client_impl.stop(timeout)

    @requires_connection
    def release_motor(self, timeout=no_timeout):
        """
        releases motor - let the motor spin freely.
        WARNING: beware of using this feature when the motor is driven (i.e. energized winding) as the
            built-up magnetic energy from the windings will cause a voltage spike on the supply bus.

        :param timeout:
            if no_timeout, fires and forget,
            else, expects a handshake reply within that time and raises otherwise
        """
        return self._aura_client_impl.release_motor(timeout)

    @requires_connection
    def reboot(self):
        """ reboots the actuator """
        self._aura_client_impl.reboot()

    @requires_connection
    def push_state_feed_freq(self, freq: hertz):
        """
        Sets the frequency at which the actuator should push its state information.
        :param freq: state feed frequency in hertz. Set to 0 for no feed.
        :return True on success
        """
        return self._aura_client_impl.configure_state_feed(hertz(freq))

    def get_state_feed_freq(self):
        """
        :return: feed state frequency 
        """
        return self._aura_client_impl.get_state_feed_freq()

    def get_latest_state(self):
        """
        the most recent state fetched from the actuator (stale if state feed if off)
        :return: feed state struct
        """
        return self._aura_client_impl.get_latest_state()

    def is_state_feed_active(self):
        """
        :return: whether state data is being pushed from the actuator
        """
        return self._aura_client_impl.is_state_feed_active()

    @requires_connection
    def stop_state_feed(self):
        """
        :return: halt state feed
        """
        return self._aura_client_impl.stop_state_feed()

    @requires_connection
    def pull_state(self, async_call: bool = False):
        """
        Fetches internal state variables from the actuator like
            temperature, current drawn, observed speed etc.
        async_call: whether to make a non-blocking call to fetch the data.
            When async_call is True, it returns a future object so that
            you should call future.get() to make a blocking call and wait
             for the data to be available.
        :return: feed state.
        """
        if async_call:
            return self._aura_client_impl.pull_state_async()
        else:
            return self._aura_client_impl.pull_state()

    @requires_connection
    def collect_phase_samples(self,
                              num_samples: int = 1000,
                              step: int = 1,
                              async_call: bool = True):
        """
        :param num_samples: number of samples to collect
        :param step: sample every other step cycles
        :param async_call: make a non-blocking call and return a future object.
        call .get() on that object to block until all samples are collected.
            example:
                future = aura_client.collect_phase_samples()
                #... some other code logic here while the samples are collected ...
                my_samples = future.get()
        :return: collected samples
        """
        if async_call:
            return self._aura_client_impl.collect_samples_async(num_samples, step)
        else:
            return self._aura_client_impl.collect_samples(num_samples, step)

    @requires_connection
    def pull_configuration(self):
        """
        :return: actuator configuration
        """
        return self._aura_client_impl.pull_configuration()

    @requires_connection
    @requires_aura_version('>0.0.10')
    def push_configuration(self, configuration, volatile_conf: bool = True):
        """
        :param configuration: configuration object
        :param volatile_conf: whether to make a temporary configuration change
            or make a permanent change (i.e. that persists across a reboot cycle).
            NOTE: it is recommended to use the permanent write (volatile_conf=False) sparingly
                 as it is slower and will end up wearing down the flash component.
        """
        if not volatile_conf:
            volatile_conf = not prompt_user_yes_no(
                "do you really want to permanently write the configuration?",
                default_yes=False)

        return self._aura_client_impl.push_configuration(configuration, store_it=not volatile_conf)

    @requires_connection
    def persist_aura_local_configuration(self):
        """
        saves the temporary configuration onto the actuator's flash
        """
        return self._aura_client_impl.persist_aura_local_configuration()

    @requires_connection
    @requires_aura_version('>=0.2.0')
    def calibrate_icmu_encoder(self, num_rotations: float = 3., debug: bool = False):
        """
        Kythera internal use only
        :param num_rotations: the number of rotation to capture
        :param debug: Whether the data should be output in csv file and the curve shall be displayed.
        """
        result = self._aura_client_impl.calibrate_icmu_encoder(num_rotations, True, debug)
        if not result:
            return False
        else:
            if debug:
                from . import show_encoder_calib
                show_encoder_calib.show_curve()

            return True

    @requires_connection
    def run_encoder_offset_detection(self, timeout_sec=1):
        return self._aura_client_impl.run_encoder_offset_detection(datetime.timedelta(timeout_sec))

    def is_in_fault_state(self):
        return self._aura_client_impl.is_in_fault_state()

    def get_current_fault(self):
        return self._aura_client_impl.get_current_fault()

    def get_latest_fault(self):
        return self._aura_client_impl.get_latest_fault()

    def set_on_fault_callback(self, callback):
        return self._aura_client_impl.set_on_fault_callback(callback)

    def impl(self):
        """
        DO NOT USE - not part of the public API
        """
        return self._aura_client_impl

    def upgrade_firmware(self,
                         version_filter: str = None,
                         update_source: str = flashage.BINARIES_DIR_PATH,
                         interactive: bool = False,
                         update_app: bool = False,
                         update_bootloader: bool = False):

        if self.aura_has_volatile_changes():
            if not self.print_volatile_changes_warning(prompt_save=True):
                if not prompt_user_yes_no("Do you want to ignore those changes and proceed with the update?",
                                          default_yes=False):
                    return False

        self.run_checks_on_disconnect = False
        return flashage.update_aura(self,
                                    version_filter=version_filter,
                                    update_source=update_source,
                                    interactive=interactive,
                                    update_app=update_app,
                                    update_bootloader=update_bootloader)


# deprecated - for backward compatibility
AuraClient.set_pwm = AuraClient.command_dutycycle
AuraClient.set_dutycycle = AuraClient.command_dutycycle
AuraClient.set_position = AuraClient.command_position
AuraClient.set_speed = AuraClient.command_speed
AuraClient.set_current = AuraClient.command_current
