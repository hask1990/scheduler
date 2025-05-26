import sched
import time
from typing import Callable, Iterable, Tuple

class Scheduler:
    """Simple wrapper around :class:`sched.scheduler`."""

    def __init__(self, timefunc: Callable[[], float] = time.time, delayfunc: Callable[[float], None] = time.sleep):
        self._scheduler = sched.scheduler(timefunc, delayfunc)

    def schedule_in(self, delay: float, action: Callable, argument: Iterable = ()):  
        """Schedule *action* to run after *delay* seconds."""
        self._scheduler.enter(delay, 1, action, argument)

    def schedule_at(self, epoch_time: float, action: Callable, argument: Iterable = ()):  
        """Schedule *action* to run at the given epoch time."""
        self._scheduler.enterabs(epoch_time, 1, action, argument)

    def run(self):
        """Run scheduled tasks until all are executed."""
        self._scheduler.run()
