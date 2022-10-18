from django.test import TestCase, Client
from rest_framework import status
import json
from doogkingapp.models import Profile


class RegistrerTestCase(TestCase):

    def test_registrer(self):
        client = Client()
        response = client.post(
            '/api/profiles/', {
                'email': 'register@gmail.com',
                'password': 'password1234',
                'first_name': 'Prova',
                'last_name': 'Testing',
            },
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(json.loads(response.content), {'email': 'register@gmail.com','password': 'password1234',
        # 'first_name': 'Prova','last_name': 'Testing','url': 'http://testserver/api/profiles/1/'})
        #print(response.content)
        # self.assertEqual(json.loads(response.content),{'url': '/api/profiles/1/'})

        # self.assertEqual(json.loads(response.content),{"{'url':'http://testserver/api/profiles/1/','email':'register@gmail.com','first_name':'Prova','last_name':'Testing'}"})


class LogInTestCase(TestCase):

    def create_Profile(self):
        return Profile.objects.create_user(email="admin@example.com", password="admin1234")

    def test_login(self):
        client = Client()
        response = client.post('/api/login/', {"username":"admin@example.com", },format='json')
        token = json.loads(response.content)
        #self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #self.assertIn("token", token)

    '''def  test_get_user(self):
        client = Client()
        response = client.get('/api/profiles/1/', {"token": }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)'''


class HousingTestCase(TestCase):

    def test_view_housing(self):
        client = Client()
        response = client.get('/api/housing/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)