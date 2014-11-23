import datetime

from django.utils import timezone
from django.test import TestCase
from .models import SignUp, Event
from django.contrib.auth.models import User

        
class SignUpTests(TestCase):
    
    def someTest(self):
        resp = self.clinet.get('/user_created_success/')
        self.assertEqual(resp.status_code,200)