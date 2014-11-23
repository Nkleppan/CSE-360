import datetime

from django.utils import timezone
from django.test import TestCase
from signups.models import SignUp, Event




class ImageSpaceTests(TestCase):

    def test_will_just_be_success(self):
        """
        Dummy test
        """
        self.assertEqual(False, False)
        
class SignUpTests(TestCase):
    
    def setUp(self):
        SignUp.objects.create(username='test',
                              password='pass',
                              email='test@local.com',
                              )
    def test_unicode(self):
        user = SignUp.objects.get(username='test')
        self.assertEqual(user.__unicode__(), 'test@local.com')