from typing import Protocol

from ..entities import Course, Lesson, Student
from ..values import DayPeriod


class CourseRepository(Protocol):

    def get(self, id: int) -> Course: ...


class LessonRepository(Protocol):

    def add(self, lesson: Lesson) -> None: ...


class RegisterForCourse:

    def __init__(self, course_id: int, student: Student, *,
                 course_repo: CourseRepository,
                 lesson_repo: LessonRepository) -> None:
        self._student = student
        self._course = course_repo.get(course_id)
        self._repo = lesson_repo

    def __call__(self) -> None:
        available_hours = self._course.get_available_hours()
        lessons = []
        for _ in range(self._course.number_of_lessons):
            lessons.append(Lesson(DayPeriod()))
