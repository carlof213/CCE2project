from django.db import models
from django.contrib.auth.models import AbstractUser
import django.contrib.auth.validators
# Create your models here.

class CustomUser(AbstractUser):
    pass
