from django.db import models
from django.db.models.signals import post_save

from django.conf import settings
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


class AccountManager(BaseUserManager):
    def create_user(self, password=None, **kwargs):
        if not kwargs.get('email') or not kwargs.get('username'):
            raise ValueError('User must have a valid email and username')        
        account = self.model(
            username=kwargs.get('username'),
            email=kwargs.get('email'),
            first_name=kwargs.get('first_name', ''),
            last_name=kwargs.get('last_name', ''),
        )

        if password is None:
            raise ValueError('User must have a valid password')
        account.set_password(password)

        account.save()
        return account


class Account(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ('time_created', )

    def __str__(self):
        return self.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Generate a token every time a new account object
    is created.
    """
    if created:
        Token.objects.create(user=instance)
