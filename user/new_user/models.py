from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, username, telephone, role, password=None):
        if not email:
            raise ValueError("Email is required!!")
        if not username:
            raise ValueError(" Username is required!! ")
        my_user = self.model(email=self.normalize_email(email), username=username, role=role, telephone=telephone)
        my_user.set_password(password)
        my_user.save()
        return my_user

class Organisation(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=500)
    slug = models.SlugField()

    def _str_(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class User(AbstractBaseUser):
    username = models.CharField(max_length=100, blank=False, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    telephone = models.CharField(max_length=13)
    role = models.CharField(max_length=30)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='staff', null=True)
    is_verified = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'telephone', 'role']

class AdminProfile(models.Model):
    organisation = models.OneToOneField(Organisation, on_delete=models.CASCADE, related_name='admin')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')














\
