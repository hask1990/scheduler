import pytest

from scheduler.core import Scheduler


def test_scheduler_order():
    executed = []
    current_time = [0.0]

    def timefunc():
        return current_time[0]

    def delayfunc(delay):
        current_time[0] += delay

    sched = Scheduler(timefunc=timefunc, delayfunc=delayfunc)
    sched.schedule_in(10, executed.append, ("task1",))
    sched.schedule_in(5, executed.append, ("task2",))

    sched.run()

    assert executed == ["task2", "task1"]
    assert current_time[0] == 10

