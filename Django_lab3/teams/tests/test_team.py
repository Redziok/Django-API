from django.test import TestCase
from base.models import Team

class PersonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
      Team.objects.create(nazwa='clowns', kraj='US')
      Team.objects.create(nazwa='sharks', kraj='CN')

    def test_first_name_label(self):
      team = Team.objects.get(id=1)
      field_label = team._meta.get_field('nazwa').verbose_name
      self.assertEqual(field_label, 'nazwa')

    def test_first_name_max_length(self):
      team = Team.objects.get(id=1)
      max_length = team._meta.get_field('kraj').max_length
      self.assertEqual(max_length, 2)

    def test_identificator_first(self):
      team = Team.objects.get(id=1)
      self.assertEqual(team.nazwa, 'clowns')

    def test_identificator_second(self):
      team = Team.objects.get(id=2)
      self.assertEqual(team.nazwa, 'sharks')
