from dataclasses import dataclass, field
import time
from typing import Callable, ClassVar, Dict, Optional
from contextlib import ContextDecorator


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


@dataclass
class Timer(ContextDecorator):
    """
    usage:
    with Timer():
        # Do something

    or:

    @Timer(name='decorator')
    def stuff():
        # Do something
    """

    timers: ClassVar[Dict[str, float]] = {}
    name: Optional[str] = None
    text: str = "Elapsed time: {:0.4f} seconds"
    logger: Optional[Callable[[str], None]] = None  # print
    _start_time: Optional[float] = field(default=None, init=False, repr=False)
    _elapsed_time: Optional[float] = field(default=None, init=False, repr=False)

    def __post_init__(self) -> None:
        """Add timer to dict of timers after initialization"""
        if self.name is not None:
            self.timers.setdefault(self.name, 0)

    def start(self) -> None:
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self) -> float:
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        # Calculate elapsed time
        self._elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

        # Report elapsed time
        if self.logger:
            self.logger(self.text.format(self._elapsed_time))
        if self.name:
            self.timers[self.name] += self._elapsed_time

        return self._elapsed_time

    def elapsed_time(self):
        if self._elapsed_time is None:
            return time.perf_counter() - self._start_time
        else:
            return self._elapsed_time

    def __enter__(self):
        """Start a new timer as a context manager"""
        self.start()
        return self

    def __exit__(self, *exc_info):
        """Stop the context manager timer"""
        self.stop()
