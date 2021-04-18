from typing import Iterable

import pytest

from ...entities import Course, Lesson, Student
from ...usecases import RegisterForCourse
from ...values import Schedule


class FakeCourseRepo:

    def __init__(self, courses: Iterable[Course]) -> None:
        self._courses = list(courses)

    def get(self, id: int) -> Course:
        return next(course for course in self._courses if id == course.id)


class FakeLessonRepo:

    def __init__(self, lessons: Iterable[Lesson]) -> None:
        self._lessons = list(lessons)

    def add(self, lesson: Lesson) -> None:
        self._lessons.append(lesson)


@pytest.fixture(scope='class')
def setup(request) -> None:
    student = Student()
    schedule = Schedule([])
    course = Course(schedule, 5, 60, [], 1)
    course_repo = FakeCourseRepo([course])
    lesson_repo = FakeLessonRepo([])
    register_for_course = RegisterForCourse(
        1,
        student,
        course_repo=course_repo,
        lesson_repo=lesson_repo
    )
    request.cls.usecase = register_for_course
    request.cls.course = course
    request.cls.repo = lesson_repo


@pytest.mark.usefixtures('setup')
class TestRegisterForCourse:

    course = Course
    repo: FakeLessonRepo

    def test_can_create_lesson_in_repo(self) -> None:
        assert len(self.repo._lessons) == self.course.number_of_lessons
