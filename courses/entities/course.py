from datetime import datetime, timedelta
from typing import List, Optional

from ..values import DayPeriod, Schedule, TimePeriod


class Student:

    def __init__(self) -> None:
        pass


class Lesson:

    def __init__(self, starts_at: datetime, duration: int,
                 course_id: int) -> None:
        self._starts_at = starts_at
        self._duration = duration
        self._course_id = course_id

    @property
    def period(self) -> DayPeriod:
        start = self._starts_at.time()
        end = (datetime.combine(self._starts_at.date(), start)
               + timedelta(minutes=self._duration)).time()
        time = TimePeriod(start, end)
        return DayPeriod(self._starts_at.weekday(), time)


class Course:

    def __init__(self, schedule: Schedule, number_of_lessons: int,
                 lesson_duration: int, registered_lessons: List[Lesson],
                 course_id: Optional[int]) -> None:
        self._schedule = schedule
        self.number_of_lessons = number_of_lessons
        self._lesson_duration = lesson_duration
        self._registered_lessons = registered_lessons
        self.id = course_id

    def get_available_hours(self) -> Schedule:
        lessons_schedule = self._get_lessons_schedule()
        return self._schedule - lessons_schedule

    def _get_lessons_schedule(self) -> Schedule:
        period = [lesson.period for lesson in self._registered_lessons]
        return Schedule(period)
