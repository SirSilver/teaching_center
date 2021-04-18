from datetime import datetime
from typing import List, Optional

from ..values import DayPeriod, Schedule


class Student:

    def __init__(self) -> None:
        pass


class Lesson:

    def __init__(self, period: DayPeriod, course_id: int) -> None:
        self.period = period
        self._course_id = course_id


class Course:

    def __init__(self, schedule: Schedule, number_of_lessons: int,
                 lesson_duration: int, lessons: List[Lesson],
                 course_id: Optional[int]) -> None:
        self._schedule = schedule
        self.number_of_lessons = number_of_lessons
        self._lesson_duration = lesson_duration
        self._lessons = lessons
        self.id = course_id

    def get_available_hours(self) -> Schedule:
        lessons_schedule = self._get_lessons_schedule()
        return self._schedule - lessons_schedule

    def _get_lessons_schedule(self) -> Schedule:
        period = [lesson.period for lesson in self._lessons]
        return Schedule(period)
