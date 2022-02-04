from django.contrib import admin
from .import models

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['email', 'name' , 'is_active', 'is_staff']

admin.site.register(models.UserProfile , UserProfileAdmin)