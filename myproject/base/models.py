from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Authors(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    dateOfBirth = models.DateField()

    def __str__(self):
        return self.name + " " + self.surname

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    releaseDate = models.DateField()

    def __str__(self):
        return self.title

class Ratings(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    bookRating = models.IntegerField(validators = [MinValueValidator(0),MaxValueValidator(5)])


