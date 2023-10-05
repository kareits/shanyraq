from django.conf import settings
from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser

from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(UserManager):
    """Manager to create custom user."""

    pass


class CustomUser(AbstractUser):
    """Custom user model."""

    phone = PhoneNumberField(
        verbose_name='phone',
        max_length=settings.PHONE_FIELD_LENGTH,
        unique=True,
        error_messages={
            'unique': 'User with this phone number already exists.',
        },
        blank=True,
    )
    email = models.EmailField(
        verbose_name='email',
        unique=True,
        error_messages={
            'unique': 'User with this email already registered',
        },
    )
    objects = CustomUserManager()

    def __str__(self):
        return self.username
