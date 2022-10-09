from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models import Model
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class Thing(Model):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'name'
    is_anonymous = False
    is_authenticated = False
    name = models.CharField(max_length = 30, unique = True, blank = False )
    description = models.TextField(unique = False, blank = True, max_length = 120)
    quantity = models.PositiveIntegerField(unique = False, validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])



