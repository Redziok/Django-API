from django.test import TestCase
from base.models import Person
from django.contrib.auth.models import User

class PersonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        Person.objects.create(imie='Jan', miesiac_urodzenia=11, owner=User.objects.get(id=1))

    def test_first_name_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('imie').verbose_name
        self.assertEqual(field_label, 'imie')

    def test_first_name_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('imie').max_length
        self.assertEqual(max_length, 50)