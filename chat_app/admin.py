from django.contrib import admin

# Register your models here.
from chat_app.models import Profile
from chat_app.models import Message

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ('user', 'photo', 'status', 'online')

admin.register(Message)