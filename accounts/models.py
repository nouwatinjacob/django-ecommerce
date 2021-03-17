from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django_countries.fields import CountryField


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)


class UserType(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_profile', on_delete=models.CASCADE,
                                verbose_name=_("user account"))
    is_admin = models.BooleanField(_("Is user an admin"), default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_address')
    full_name = models.CharField(_("user full name"), max_length=100, blank=True, default='')
    address1 = models.CharField(_("address1"), max_length=100, blank=True, default='')
    address2 = models.CharField(_("address2"), max_length=100, blank=True, default='')
    postcode = models.CharField(_("Postal Code"), max_length=50, blank=True, default='')
    city = models.CharField(_("city"), max_length=100, blank=True, default='')
    state = models.CharField(_("state"), max_length=100, blank=True, default='')
    country = CountryField(_("country"), blank=True, default='NG')
    phone = models.CharField(_("phone number"), max_length=20, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)