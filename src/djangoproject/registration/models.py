'''
Created on May 25, 2019

@author: shanti
'''
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from django.utils import timezone
from localflavor.us.models import USStateField, STATE_CHOICES, USPostalCodeField
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField

class Address(models.Model):
    user = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30, default="")
    state = USStateField(choices=STATE_CHOICES)
    zipcode = USPostalCodeField()
    country = models.CharField(max_length=50, default="")

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Address'

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            is_active=True,
            date_joined=timezone.now(),
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(
            email=email,
            is_staff=True,
            is_superuser=True,
            is_active=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):

    USERNAME_FIELD = 'email'

    objects = UserManager()
    userid = models.CharField(max_length=255)
    email = models.EmailField('email', unique=True)
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    is_staff = models.BooleanField('staff status', default=False,
                                   help_text='Designates whether the user can log into this admin '
                                               'site.')
    is_active = models.BooleanField('active', default=True,
                                    help_text='Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting account.')
    is_referrer = models.BooleanField('referrer', default=True,
                                    help_text='Designates whether this user should be treated as a Referrer '
                                              'account. Unselect this instead of deleting account.')

    def get_full_name(self):
        full_name = str(self.email)
        return full_name

    def __str__(self):
        return self.get_full_name()

    def to_domain(self):
        return domain_model.User(
            orderid=self.userid, sku=self.sku, qty=self.qty
        )

    @property
    def username(self):
        full_name = self.email
        return full_name
    
    @property
    def userid(self):
        return self.id

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = PhoneNumberField(null=True, validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$')])


