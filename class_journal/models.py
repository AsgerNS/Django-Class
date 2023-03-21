from django.db import models
from django.contrib.auth.models import User


class Class(models.Model):
    objects = None
    name = models.CharField(max_length=10)
    year = models.IntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classes = models.ManyToManyField(Class)
    age = models.IntegerField()
    subjects = models.ManyToManyField('Subject', through='Grade')

    def __str__(self):
        return self.user.username


class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.CharField(max_length=1, choices=(
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
    ))

    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.subject.name} - {self.grade}"
