from rest_framework import status
from rest_framework.test import APITestCase
from base.models import Person
from django.contrib.auth.models import User

class PersonTests(APITestCase):

    def test_create_person(self):
      User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
      url='/persons/'
      data = {'imie': 'marek', 'miesiac_urodzenia': 11, 'owner': User.objects.get(id=1).pk}
      response = self.client.post(url, data, format='json')
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      self.assertEqual(Person.objects.count(), 1)
      self.assertEqual(Person.objects.get().nazwa, 'John')
