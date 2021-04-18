from datetime import date, datetime, timedelta
from typing import List, Optional

from ..values import DayPeriod, Schedule, TimePeriod


class Student:

    def __init__(self) -> None:
        pass


class Lesson:

    def __init__(self, starts_at: datetime, duration: int,
                 course_id: int) -> None:
        self.starts_at = starts_at
        self._duration = duration
        self._course_id = course_id

    @property
    def period(self) -> DayPeriod:
        start = self.starts_at.time()
        end = (datetime.combine(self.starts_at.date(), start)
               + timedelta(minutes=self._duration)).time()
        time = TimePeriod(start, end)
        return DayPeriod(self.starts_at.weekday(), time)


class Course:

    def __init__(self, schedule: Schedule, number_of_lessons: int,
                 lesson_duration: int, registered_lessons: List[Lesson],
                 course_id: int = None) -> None:
        self._schedule = schedule
        self._number_of_lessons = number_of_lessons
        self.lesson_duration = lesson_duration
        self._registered_lessons = registered_lessons
        self.id = course_id

    def get_available_hours(self, from_date: date) -> Schedule:
        lessons_schedule = self._get_lessons_schedule(from_date)
        return self._schedule - lessons_schedule

    def _get_lessons_schedule(self, from_date: date) -> Schedule:
        period = [lesson.period for lesson in self._registered_lessons
                  if lesson.starts_at >= from_date]
        return Schedule(period)

    def __len__(self) -> int:
        return self._number_of_lessons
