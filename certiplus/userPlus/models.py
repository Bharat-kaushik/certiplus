from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from timezone_field import TimeZoneField
from django.core.validators import RegexValidator
from encrypted_fields import fields
import uuid


alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


class Country(models.Model):
    Name = models.CharField(_('Name'), max_length=100, null=True)

    def __str__(self):
        return self.Name

    class Meta:
        db_table = 'countries'
        verbose_name = _('country')
        verbose_name_plural = _('countries')


class Company(models.Model):
    key = models.CharField(max_length=10, editable=False, default=str(uuid.uuid4())[0:10], unique=True, validators=[alphanumeric])
    Company_Name = models.CharField(_('Company Name'), max_length=100, null=True,)
    Legal_Name = models.CharField(_('Legal Name'), max_length=100, null=True,)
    PAN_CARD = models.CharField(_('PAN Card'), max_length=30, null=True)
    Tax_ID = models.CharField(_('Tax ID'), max_length=50, null=True)
    user_name = models.CharField(_('User Name'), max_length=50, null=True,)
    mobile = models.CharField(_('Mobile'), max_length=40, null=True)
    Address_Line_1 = models.CharField(_('Address Line 1'), max_length=50, null=True)
    Address_Line_2 = models.CharField(_('Address Line 2'), max_length=50, null=True)
    Locality = models.CharField(_('Locality'), max_length=50, null=True)
    City = models.CharField(_('City'), max_length=50, null=True,)
    State = models.CharField(_('State'), max_length=50, null=True,)
    Country = models.ForeignKey(Country, on_delete=models.CASCADE,null=True)
    Postal_Code = models.IntegerField(_('Postal Code'), null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'company'
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")

    def __str__(self):
        return self.Company_Name


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **kwargs):
        if not username:
            raise ValueError("Not a valid Mobile Number")
        username = self.normalize_email(username)
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.key = str(uuid.uuid4())[0:9]
        user.save(using=self._db)
        return user

    # def create_user(self, mobile, password=None, **kwargs):
    #     kwargs.setdefault('is_superuser', False)
    #     kwargs.setdefault('is_staff', False)
    #     return self._create_user(mobile, password, **kwargs)

    def create_superuser(self, username, password, **kwargs):
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_Verified', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    key = models.CharField(max_length=10, null=True, editable=False, default=str(uuid.uuid4())[0:10], unique=True, validators=[alphanumeric])
    username =  models.CharField(_('Username'), max_length=30,null=True, unique=True)
    email = fields.EncryptedEmailField(_('email address'))
    name = fields.EncryptedCharField(_('Name'), max_length=30, blank=True)
    # phone_regex = RegexValidator(regex=r'^\?1?\d{9,15}$',
    #                              message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile = models.CharField(_('Mobile'),  max_length=17, )
    created_on = models.DateTimeField(_('created_on'), auto_now_add=True, null=True)
    updated_on = models.DateTimeField(_('updated_on'), auto_now=True, null=True)
    is_Verified = models.BooleanField(_('Is_Verified'), default=False)
    is_active = models.BooleanField(_('active'), default=False)
    first_login = models.BooleanField(default=False)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_superuser = models.BooleanField(_('superuser'), default=False)
    timezone = TimeZoneField(default="Indian/Christmas")
    last_login_ip = models.GenericIPAddressField(blank=True, null=True)


    objects = UserManager()

    # objects = models.Manager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email']

    class Meta:
        db_table = 'Users'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        return self.name

    def get_mobile(self):
        return self.mobile

    def set_random_password(self):
        password = UserManager().make_random_password()
        self.set_password(password)
        return password

    def __str__(self):
        return self.get_full_name()

class Otp(models.Model):
    otp = models.IntegerField(_('otp'),null=True)
    otp_time = models.DateTimeField(_('otp_Time'), null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    counter = models.IntegerField(_('counter'), null=True)





    def __str__(self):
        return str(self.user)


class Logo(models.Model):
    # logo  = models.OneToOneField(User,on_delete=models.CASCADE,default="" )
    image = models.ImageField(upload_to="logo/images", default="")



