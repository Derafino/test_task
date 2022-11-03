from django.db import models
from django.contrib.auth.admin import User


class UserAvatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.URLField(max_length=200)
