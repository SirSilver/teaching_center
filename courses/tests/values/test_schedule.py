from datetime import time

import pytest

from ...values import DayPeriod, Schedule, TimePeriod


@pytest.fixture(scope='class')
def setup(request) -> None:
    period_1 = DayPeriod(day=1, time=TimePeriod(time(9, 0, 0), time(18, 0, 0)))
    period_2 = DayPeriod(day=2, time=TimePeriod(time(9, 0, 0), time(18, 0, 0)))
    request.cls.schedule = Schedule([period_1, period_2])


@pytest.mark.usefixtures('setup')
class TestSchedule:

    schedule: Schedule

    def test_can_find_period_for_a_day(self) -> None:
        result = self.schedule.find_period_for_day(1)
        assert result.time.start.hour == 9
        assert result.time.start.minute == 0
        assert result.time.start.second == 0

    def test_can_subtract_schedule(self) -> None:
        period = DayPeriod(day=1, time=TimePeriod(time(9, 0, 0), time(10, 0, 0)))
        schedule = Schedule([period])
        result = self.schedule - schedule
        assert result.periods[0].time.start.hour == 10
        assert result.periods[0].time.start.minute == 0
        assert result.periods[0].time.start.second == 0
