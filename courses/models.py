from django.db import models


class Hours(models.Model):
    starts_at = models.TimeField('Start time')
    ends_at = models.TimeField('End time')

    class Meta:
        verbose_name = 'Hours'
        verbose_name = 'Hours'

    def __str__(self):
        return f'{self.starts_at} - {self.ends_at}'


class DayPeriod(models.Model):

    day = models.SmallIntegerField('Day of the week')
    period = models.ForeignKey(
        verbose_name='Time period',
        to=Hours,
        on_delete=models.CASCADE,
        related_name='+'
    )


class Teacher(models.Model):

    working_schedule = models.ManyToManyField(
        verbose_name='Working time',
        to=DayPeriod
    )

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return f'Teacher {self.id}'


class Course(models.Model):

    teacher = models.ForeignKey(
        verbose_name='Teacher',
        to=Teacher,
        on_delete=models.CASCADE,
        related_name='courses',
    )
    available_at = models.ManyToManyField(
        verbose_name='Available hours',
        to=DayPeriod
    )
    number_of_lessons = models.PositiveSmallIntegerField('Number of lessons')

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return f'Course {self.id} - {self.teacher}'


class Student(models.Model):

    course = models.ForeignKey(
        verbose_name='Course',
        to=Course,
        on_delete=models.CASCADE,
        related_name='students'
    )

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return f'Student {self.id} - {self.course}'


class Lesson(models.Model):

    course = models.ForeignKey(
        verbose_name='Course',
        to=Course,
        on_delete=models.CASCADE,
        related_name='lessons'
    )
    starts_at = models.DateTimeField('Beginning time')
    duration = models.PositiveSmallIntegerField('Duration')
    student = models.OneToOneField(
        verbose_name='Student',
        to=Student,
        on_delete=models.CASCADE,
        related_name='lessons'
    )

    class Meta:
        verbose_name = 'Course lesson'
        verbose_name_plural = 'Course lessons'

    def __str__(self):
        return f'Lesson - {self.course}'
