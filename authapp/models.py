from django.db import models
from django.contrib.auth.models import AbstractUser

import pytz
from django.conf import settings
from datetime import datetime, timedelta

class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name = 'возраст')

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(auto_now_add=True)

    def is_activation_key_expired(self):
        if datetime.now(pytz.timezone(settings.TIME_ZONE)) < (self.activation_key_expires + timedelta(hours=48)):
            return False
        return True
