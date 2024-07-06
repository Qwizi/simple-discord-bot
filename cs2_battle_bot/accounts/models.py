from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from prefix_id import PrefixIDField


# Create your models here.

class Account(AbstractUser, PermissionsMixin):
    id = PrefixIDField(prefix="account", primary_key=True)
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='account_set',
        related_query_name='account',
        verbose_name='user permissions'
    )

    def __str__(self):
        return f"{self.username}"