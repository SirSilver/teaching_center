from datetime import time

import pytest

from ...entities import Course, Lesson
from ...values import DayPeriod, Schedule, TimePeriod


@pytest.fixture(scope='class')
def setup(request) -> None:
    period_1 = DayPeriod(day=1, time=TimePeriod(time(9, 0, 0), time(18, 0, 0)))
    period_2 = DayPeriod(day=2, time=TimePeriod(time(9, 0, 0), time(18, 0, 0)))
    periods = [period_1, period_2]
    schedule = Schedule(periods)
    period = DayPeriod(1, TimePeriod(time(9, 0, 0), time(10, 0, 0)))
    lessons = [Lesson(period, 1)]
    request.cls.course = Course(schedule, 5, 60, lessons, 1)


@pytest.mark.usefixtures('setup')
class TestCourse:

    course: Course

    def test_can_find_available_hours(self) -> None:
        result = self.course.get_available_hours()
        print(result.periods)
        assert result.periods[0].time.start.hour == 10
        assert len(result.periods) == 2
