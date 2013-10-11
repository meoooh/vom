"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from vom.models import *

class SimpleTest(TestCase):
    def setUp(self):
        Constellation.objects.create(name='test', dot=3)

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 1)

    def test_user_creation(self):
        response = self.client.post('/join', {
            'email': 'a@a.com',
            'name': 'a',
            'birthday': '1990-06-17',
            'sex': '1',
            'password2': '1313',
            'password': '1313'
        })

        self.assertEqual(response.status_code, 302)
