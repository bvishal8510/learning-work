from django.test import TestCase
from .models import Profile, Document, Comments
 
class ProfileModelTests(TestCase):
 
   def test1(self):
 
       user_profile = Profile(First_Name='Surya', Last_Name='Sarma')
       self.assertIs(user_profile.First_Name == 'Surya', True)
 
class DocumentModelTests(TestCase):
  
   def test1(self):
 
       user_document = Document(blur = 'n', like_or_not=1)
       self.assertIs(user_document.blur == 'n', True)
       self.assertIs(user_document.like_or_not == 1, True)
 
class DocumentModelTests(TestCase):
  
   def test1(self):
 
       user_comment = Comments(comment='nice work')
       self.assertIs(user_document.comment == 'nice work', True)
