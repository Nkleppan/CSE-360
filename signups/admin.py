from django.contrib import admin

# Register your models here.
from .models import SignUp, Event, Setting


class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model = SignUp
        
class EventAdmin(admin.ModelAdmin):
    class Meta:
        model = Event
    
        
class SettingAdmin(admin.ModelAdmin):
    class Meta:
        model = Setting
        
        
admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Setting, SettingAdmin)