from django.db import models
from django import forms


class Course(models.Model):
    title = models.CharField(max_length=20)

class Student(models.Model):
    name = models.CharField(max_length=10)
    group = models.CharField(max_length=4)
    course = models.ManyToManyField(Course)