from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.conf import settings

class UserManager(BaseUserManager):

    def _create_user(self, name, email, password, is_staff, is_superuser, is_active, **extra_fields):
        # if not email:
        #     raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            name=name,
            email=email,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, name, email, password=None, **extra_fields):
        return self._create_user(name, email, password, False, False, True, **extra_fields)

    def create_superuser(self, name, password, email=None, **extra_fields, ):
        user = self._create_user(name, email, password, True, True, True, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=False, blank=True)
    name = models.CharField(max_length=254, null=True, blank=True, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'name'
    # EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
