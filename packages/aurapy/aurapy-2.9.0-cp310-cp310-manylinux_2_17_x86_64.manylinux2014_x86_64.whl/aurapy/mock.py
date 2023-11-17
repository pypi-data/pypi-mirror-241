from .auraclient import AuraClient
from ._aura_pybind import register_mock_device, unregister_mock_device, is_mock_port
from ._aura_pybind import list_mock_ports, mock_device_registry
from functools import wraps


def is_any_aura_connected():
    c = AuraClient()
    board_is_connected = c.connect(silent=True)
    if board_is_connected:
        c.disconnect()
    del c
    return board_is_connected


def print_mock_state():
    reg = mock_device_registry()
    for a, b in reg.items():
        print(a, b.sim_instance.description())


class AuraSimPortContext:
    """
        a context + decorator class to manage insertion/removal of mock aura ports

        usage:
            with AuraSimPortContext() as simContext:
                with AuraClient() as client:
                    print("connected to mock client on", simContext.port_name)
    """

    def __init__(self, sim_spec="COM_TEST", track_real_time=True, verbose_level=0):
        """
        :param sim_spec: if empty, no mocking is used
        :param verbose_level: aura mock verbosity level - 0 is the least verbose level
        """
        self._sim_spec = sim_spec
        self._verbose_level = verbose_level
        self._track_real_time = track_real_time
        self._mock_entry = None

    def is_active(self):
        return self._mock_entry is not None

    @property
    def port_name(self):
        assert(self.is_active()), "context is not active"
        return self._mock_entry.port_name

    @property
    def sim_instance(self):
        assert(self.is_active()), "context is not active"
        return self._mock_entry.sim_instance

    def create_sim(self):
        """
        instantiate simulated instances as per specifications provided
        :return:
        """
        self._mock_entry = register_mock_device(port_spec=self._sim_spec,
                                                track_real_time=self._track_real_time)
        self._mock_entry.sim_instance.set_verbose(self._verbose_level)

    def clear_sim(self):
        """
        tear down simulated instances
        :return:
        """
        if self._mock_entry:
            unregister_mock_device(self._mock_entry.port_name)
            self._mock_entry = None

    def __enter__(self):
        if self._sim_spec:
            self.create_sim()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.clear_sim()

    def __call__(self, func):
        """ meant to be used as a decorator """
        @wraps(func)
        def wrapped(*args, **kwargs):
            with self:
                return func(*args, **kwargs)

        return wrapped

    def __del__(self):
        self.clear_sim()


with_aura_sim = AuraSimPortContext
