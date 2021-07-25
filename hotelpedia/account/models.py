from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, fname, lname, password, **extra_fields):

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            fname=fname,
            lname=lname,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, fname, lname, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, fname, lname, password, **extra_fields)

    def create_superuser(self, email, fname, lname, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, fname, lname, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    fname = models.CharField(max_length=128)
    lname = models.CharField(max_length=128)
    phone = PhoneNumberField(blank=True, null=True, unique=True)
    bday = models.CharField(max_length=128, blank=True, null=True)
    country = CountryField(blank_label="Select the country/region you're from", blank=True, null=True)
    GENDER_CHOICES = (
        ("man", "Man"),
        ("female", "Female"),
        ("non_binary", "Non-binary"),
        ("prefer_not_to_say", "Prefer not to say"),
    )

    gender = models.CharField(max_length=20,
                  choices=GENDER_CHOICES,
                  default="prefer_not_to_say")
    picture = models.ImageField(upload_to='images/%Y/%m/%d/', default="images/profile.png", blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fname', 'lname']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.fname.split()[0]