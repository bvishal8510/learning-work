from django.test import TestCase
import datetime
from django.utils import timezone

from .models import Profile, Document, Comments


class ProfileModelTests(TestCase):

    def test1(self):

        user_profile = Profile(First_Name='Varsha', Last_Name='Baghel')
        self.assertIs(user_profile.First_Name == 'Varsha', True)
