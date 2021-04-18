from datetime import date, datetime, timedelta
from typing import Protocol

from ..entities import Course, Lesson, Student
from ..values import DayPeriod


class CourseRepository(Protocol):

    def get(self, id: int) -> Course: ...


class LessonRepository(Protocol):

    def add(self, lesson: Lesson) -> None: ...


class RegisterForCourse:

    def __init__(self, course_id: int, student: Student, timeout: int, *,
                 course_repo: CourseRepository,
                 lesson_repo: LessonRepository) -> None:
        self._student = student
        self._course = course_repo.get(course_id)
        self._timeout = timeout
        self._repo = lesson_repo

    def __call__(self) -> None:
        from_date = date.today() + timedelta(days=self._timeout)
        available_hours = self._course.get_available_hours(from_date)
        for _ in range(len(self._course)):
            for period in available_hours.periods:
                available_hours.find_period_for_day(from_date.weekday())
            starts_at = from_date
            lesson = Lesson(starts_at, self._course.lesson_duration, self._course.id)
