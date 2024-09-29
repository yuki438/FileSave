from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, login, password=None, **extra_fields):
        if not login:
            raise ValueError('Login is Required')
        if self.model.objects.filter(login=login).exists():
            raise ValueError('Login already exists')
        user = self.model(login=login, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, login, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(login, password, **extra_fields)

class UserData(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.login