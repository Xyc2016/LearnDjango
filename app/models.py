from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=16)
    age = models.IntegerField()


class Comment(models.Model):
    content = models.CharField(max_length=1000)


class Member(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)


class Animal(models.Model):
    name = models.CharField(max_length=16)
    sound = models.CharField(max_length=16)

    def speak(self):
        return f'The {self.name} says \"{self.sound}\"'
