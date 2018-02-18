from django.test import TestCase
import unittest
from django.test import Client
from .models import Profile, Document, Comments


class ProfileModelTests(TestCase):

    def test1(self):

        user_profile = Profile(First_Name='Varsha', Last_Name='Baghel')
        self.assertIs(user_profile.First_Name == 'Varsha', True)

class DocumentModelTests(TestCase):
    
    def test1(self):

        user_document = Document(blur = 'n', like_or_not=1)
        self.assertIs(user_document.blur == 'n', True)
        self.assertIs(user_document.like_or_not == 1, True)

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/phoics/profile/robinhood')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        # self.assertEqual(len(response.context['customers']), 5)