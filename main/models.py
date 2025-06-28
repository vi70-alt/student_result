from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=10)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.user.username} - {self.subject}"
