from django.contrib import admin
from .models import UserProfile, UserSettings

admin.site.register([UserProfile, UserSettings])