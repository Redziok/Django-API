from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models

class Druzyna(models.Model):
    nazwa = models.CharField(max_length=50)
    kraj = models.CharField(max_length=2)

    def __str__(self):
        return self.nazwa

class Persons(models.Model):

    miesiace = models.IntegerChoices('miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    miesiac_urodzenia = models.IntegerField(choices=miesiace.choices, default = '1')
    data_dodania = models.DateField(auto_now_add=True)
    Drużyna = models.ForeignKey(Druzyna, on_delete=models.SET_NULL, null = True)

    class Meta:
        ordering = ["nazwisko"]