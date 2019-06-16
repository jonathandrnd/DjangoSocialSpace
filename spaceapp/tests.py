from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_signup(self):
        # Issue a GET request.
        response = self.client.get('/spaceapp/signup/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code,200)

    def test_login(self):
        # Issue a GET request.
        response = self.client.get('/spaceapp/login/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code,200)

class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'user',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/spaceapp/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

class LogoutTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'user',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/spaceapp/login/', self.credentials, follow=True)
        # Now logout user logged
        response = self.client.post('/spaceapp/logout/', self.credentials, follow=True)
        # sould be logout now
        self.assertFalse(response.context['user'].is_active)
