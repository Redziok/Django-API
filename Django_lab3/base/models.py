from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Team(models.Model):
    nazwa = models.CharField(max_length=50)
    kraj = models.CharField(max_length=2)

    def __str__(self):
        return self.nazwa

class Person(models.Model):

    miesiace = models.IntegerChoices('miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    miesiac_urodzenia = models.IntegerField(choices=miesiace.choices, default = '1')
    data_dodania = models.DateField(auto_now_add=True)
    Drużyna = models.ForeignKey(Team, on_delete=models.SET_NULL, null = True)
    owner = models.ForeignKey(User, related_name='persons', on_delete=models.CASCADE)

    class Meta:
        ordering = ["nazwisko"]

    def __str__(self):
        return self.imie + " " + self.nazwisko

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

