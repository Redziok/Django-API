from rest_framework import status
from rest_framework.test import APITestCase
from base.models import Team

class TeamTests(APITestCase):
    def test_create_team(self):
        url = '/teams/'
        data = {'nazwa': 'dogs', 'kraj': 'PLN'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(Team.objects.get().nazwa, 'DabApps')