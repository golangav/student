from django.db import models


class Userinfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)


class Classes(models.Model):
    title = models.CharField(max_length=32)


class Student(models.Model):
    name = models.CharField(max_length=32)
    age = models.CharField(max_length=32)
    cls = models.ForeignKey(to="Classes",to_field="id")


