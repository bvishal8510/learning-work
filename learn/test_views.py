import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
       def setUp(self):
       self.client = Client()
