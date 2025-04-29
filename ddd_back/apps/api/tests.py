from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User

class LoginEndpointTest(APITestCase):
    def setUp(self):
        self.username = "analyst"
        self.password = "analyst"
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.client = APIClient()
        self.url = 'http://localhost:8000/api/auth/login/'

    def test_login_success(self):
        data = {
            "username": self.username,
            "password": self.password
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)

    def test_login_fail(self):
        data = {
            "username": self.username,
            "password": "mauvais_mot_de_passe"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
