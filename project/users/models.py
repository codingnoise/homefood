from __future__ import unicode_literals

from django.utils import timezone
import urllib

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
# from django.db.models.signals import post_save
# from django.dispatch import receiver


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, name, password, is_staff, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        print "here"
        user = self.model(email=email,
                          name=name,
                          is_staff=is_staff,
                          is_active=True,
                          last_login=now,
                          date_joined=now,
                          **extra_fields)

        print "here2"
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, name, password, False, **extra_fields)

    def create_superuser(self, email, name, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
             raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, name, password, True, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email =  models.EmailField(unique=True)
    name = models.CharField(max_length=40, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/user/%s" % urllib.quote(self.email)

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s' % self.name
        return full_name.strip()

    def get_short_name(self):
        full_name = '%s' % self.name
        return full_name.strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)