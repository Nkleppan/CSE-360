from django.contrib import admin

# Register your models here.
from .models import SignUp, Event


class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model = SignUp
        
class EventAdmin(admin.ModelAdmin):
    class Meta:
        model = Event
    
        
admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Event, EventAdmin)