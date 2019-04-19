# coding: utf-8

from django.db import models
from django.contrib.auth.models import AbstractUser

class ChatUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    contacts = models.CharField(verbose_name='contacts', max_length=255, unique=True, default='test user')