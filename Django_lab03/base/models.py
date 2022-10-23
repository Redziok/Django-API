from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Authors(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    dateOfBirth = models.DateField()

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    releaseDate = models.DateField()

class Ratings(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    bookRating = models.IntegerField(validators = [MinValueValidator(0),MaxValueValidator(5)])

class Persons(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    miesiac_urodzenia = models.IntegerChoices('miesiac_urodzenia', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')
    data_dodania = models.DateField(auto_now_add=True)
    kraj = models.ForeignKey(Druzyna, on_delete=models.SET_NULL)

    class Meta:
        ordering = ["nazwisko"]

class Druzyna(models.Model):
    nazwa = models.CharField(max_length=50)
    kraj = models.CharField(max_length=2)
