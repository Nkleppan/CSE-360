from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class SignUp(models.Model):
    user = models.OneToOneField(User)
    profilePic = models.ImageField(upload_to='profilePics/', blank=True, null=True, default='profilePics/default.png')
    
    def __unicode__(self):
        return self.user.username
    
User.profile = property(lambda u: SignUp.objects.get_or_create(user=u)[0])

class Event(models.Model):
    title = models.CharField(max_length=40)
    type = models.CharField(max_length=16)
    venue = models.CharField(max_length=40)
    date = models.DateField()
    time = models.TimeField()
    current_avail = models.IntegerField(default=0)
    total_avail = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title