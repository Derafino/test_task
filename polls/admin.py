from django.contrib import admin
from .models import UserAvatar


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar']


admin.site.register(UserAvatar, CustomUserAdmin)
