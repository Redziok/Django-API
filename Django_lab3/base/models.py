from email.policy import default
from random import choices
from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

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
    owner = models.ForeignKey('auth.User', related_name='persons', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ["nazwisko"]

    def __str__(self):
        return self.imie + " " + self.nazwisko

    def save(self, *args, **kwargs):
        imie = self.imie
        nazwisko = self.nazwisko
        miesiac_urodzenia = self.miesiac_urodzenia
        formatter = HtmlFormatter(style=self.style, nazwisko=nazwisko,
                                  full=True, **miesiac_urodzenia)
        self.highlighted = highlight(self.code, imie, formatter)
        super().save(*args, **kwargs)

