from django import forms
from .models import SignUp
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required = True)
    username = forms.CharField(max_length=32, required=True)
    
    
    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}
    
    
    def save(self,commit = False):   
        user = super(SignUpForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        
        
        if commit:
            user.save()

        return user
    
    
class SettingsForm(forms.Form):
    image = forms.ImageField(required=True)