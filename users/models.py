from uuid import uuid4

from django.contrib.auth.models import PermissionsMixin
from django.db import models as md
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from mlechniy_put.constants import DbFieldsLength
from mlechniy_put.models import BaseAbstractModel
from users.managers import CustomUserManager


class UserProfile(
    BaseAbstractModel,
):
    first_name = md.CharField(_("first name"), max_length=DbFieldsLength.CHAR_FIELD)
    last_name = md.CharField(_("last name"), max_length=DbFieldsLength.CHAR_FIELD)
    patronymic = md.CharField(
        _("patronymic name"),
        max_length=DbFieldsLength.CHAR_FIELD,
        null=True,
        blank=True,
    )
    phone = md.CharField(_("phone number"), max_length=11)
    age = md.IntegerField(_("age"))
    post_address_author = md.CharField(
        _("author's post address"),
        max_length=DbFieldsLength.CHAR_FIELD,
        null=True,
        blank=True,
    )
    edu_organization_name = md.CharField(
        _("educational organization name"),
        max_length=DbFieldsLength.CHAR_FIELD,
        null=True,
        blank=True,
    )
    edu_organization_address = md.CharField(
        _("educational organization address"),
        max_length=DbFieldsLength.CHAR_FIELD,
        null=True,
        blank=True,
    )
    teacher_full_name = md.CharField(
        _("teacher full name"),
        max_length=DbFieldsLength.CHAR_FIELD,
        null=True,
        blank=True,
    )
    teacher_position = md.CharField(
        _("teacher's position"),
        max_length=DbFieldsLength.CHAR_FIELD,
        null=True,
        blank=True,
    )

    def get_full_name(self):
        if self.patronymic:
            return f"{self.last_name} {self.first_name} {self.patronymic}"
        else:
            return f"{self.last_name} {self.first_name}"

    def get_short_name(self):
        if self.patronymic:
            return f"{self.last_name} {self.first_name[0]}.{self.patronymic[0]}."
        else:
            return f"{self.last_name} {self.first_name[0]}."

    def __str__(self):
        return self.get_full_name()


class CustomUser(AbstractBaseUser, PermissionsMixin, BaseAbstractModel):
    ADMIN = 1
    ADJUDICATOR = 2
    PARTICIPANT = 3

    ROLE_CHOICES = [
        (ADMIN, _("Admin")),
        (ADJUDICATOR, _("Adjudicator")),
        (PARTICIPANT, _("Participant")),
    ]

    email = md.EmailField(_("email address"), unique=True)
    password = md.CharField(_("password"), max_length=88)
    is_staff = md.BooleanField(_("is staff"), default=False)
    is_active = md.BooleanField(_("is active"), default=True)
    user_type = md.IntegerField(
        _("user type"), choices=ROLE_CHOICES, default=PARTICIPANT
    )

    uuid = md.UUIDField(default=uuid4, editable=False, unique=True)

    profile = md.OneToOneField(UserProfile, on_delete=md.CASCADE, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        if self.profile is not None:
            return f"{self.profile.get_short_name()} - {self.get_user_type_display()}"
        return f"{self.email} - {self.get_user_type_display()}"
