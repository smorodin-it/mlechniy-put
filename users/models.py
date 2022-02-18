from uuid import uuid4

from django.db import models as md
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from mlechniy_put.constants import DbFieldsLength
from mlechniy_put.models import BaseAbstractModel
from users.managers import CustomUserManager


class Role(BaseAbstractModel):
    ADMIN = 1
    ADJUDICATOR = 2
    PARTICIPANT = 3

    ROLE_CHOICES = [
        (ADMIN, _('Admin')),
        (ADJUDICATOR, _('Adjudicator')),
        (PARTICIPANT, _('Participant')),
    ]

    role_name = md.IntegerField(_('role'), choices=ROLE_CHOICES, default=PARTICIPANT)


class Profile(BaseAbstractModel):
    first_name = md.CharField(_('first name'), max_length=DbFieldsLength.CHAR_FIELD)
    last_name = md.CharField(_('last name'), max_length=DbFieldsLength.CHAR_FIELD)
    patronymic = md.CharField(_('patronymic name'), max_length=DbFieldsLength.CHAR_FIELD, null=True)
    phone = md.CharField(_('phone number'), max_length=11)
    age = md.IntegerField(_('age'),)
    post_address_author = md.CharField(_('author\'s post address'), max_length=DbFieldsLength.CHAR_FIELD)
    edu_organization_name = md.CharField(_('educational organization name'), max_length=DbFieldsLength.CHAR_FIELD, null=True)
    edu_organization_address = md.CharField(_('educational organization address'), max_length=DbFieldsLength.CHAR_FIELD, null=True)
    teacher_full_name = md.CharField(_('teacher full name'), max_length=DbFieldsLength.CHAR_FIELD, null=True)
    teacher_position = md.CharField(_('teacher\'s position'), max_length=DbFieldsLength.CHAR_FIELD, null=True)

    def get_full_name(self):
        return f'${self.last_name} ${self.first_name} ${self.patronymic}'

    def get_short_name(self):
        return f'${self.last_name} ${self.first_name[0]}.${self.patronymic[0]}.'


class CustomUser(AbstractBaseUser, PermissionsMixin, BaseAbstractModel):
    email = md.EmailField(_('email address'), unique=True)
    password = md.CharField(_('password'), max_length=88)
    is_staff = md.BooleanField(_('is staff'), default=False)
    is_active = md.BooleanField(_('is active'), default=True)
    uuid = md.UUIDField(default=uuid4(), editable=False, unique=True)

    role = md.ForeignKey(Profile, on_delete=md.CASCADE, related_name=_('users'))
    profile = md.OneToOneField(Profile, on_delete=md.CASCADE, null=True, default=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_text_role(self):
        return self.role

    def __str__(self):
        if self.profile is not None:
            return f'{self.profile.get_short_name()} - {self.get_text_role()}'
        return f'{self.email} - {self.get_text_role()}'
