from datetime import datetime, time

import pytest

from ...entities import Course, Lesson
from ...values import DayPeriod, Schedule, TimePeriod


@pytest.fixture(scope='class')
def setup(request) -> None:
    period_1 = DayPeriod(day=0, time=TimePeriod(time(9, 0, 0), time(18, 0, 0)))
    period_2 = DayPeriod(day=1, time=TimePeriod(time(9, 0, 0), time(18, 0, 0)))
    periods = [period_1, period_2]
    schedule = Schedule(periods)
    lessons = [Lesson(datetime(2021, 4, 19, 9, 0, 0), 60, 1),
               Lesson(datetime(2021, 4, 20, 9, 0, 0), 60, 1)]
    request.cls.course = Course(schedule, 5, 60, lessons, 1)


@pytest.mark.usefixtures('setup')
class TestCourse:

    course: Course

    def test_can_find_available_hours(self) -> None:
        result = self.course.get_available_hours()
        assert result.periods[0].time.start.hour == 10
        assert result.periods[1].time.start.hour == 10
        assert len(result.periods) == 2
