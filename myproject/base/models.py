from datetime import date
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Users(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    dateOfBirth = models.DateField()

class Authors(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    dateOfBirth = models.DateField()

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    releaseDate = models.DateField()

class Ratings(models.Model):
    User = models.ForeignKey(Users, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    bookRating = models.IntegerField(validators = [MinValueValidator(0),MaxValueValidator(5)])


