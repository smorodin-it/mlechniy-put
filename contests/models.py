from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models as md
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from mlechniy_put.constants import DbFieldsLength
from mlechniy_put.models import BaseAbstractModel
from users.models import CustomUser


class Contest(BaseAbstractModel, PermissionsMixin):
    title = md.CharField(_("contest title"), max_length=DbFieldsLength.CHAR_FIELD)
    description = md.TextField(
        _("contest description"), max_length=DbFieldsLength.TEXT_FIELD
    )
    start_date = md.DateField(_("contest start date"), null=True, blank=True)
    end_date = md.DateField(_("contest end date"), null=True, blank=True)
    active = md.BooleanField(_("active"), default=False)
    adjudicators = md.ManyToManyField(
        CustomUser, related_name="adjudicator_in_contests"
    )
    participants = md.ManyToManyField(
        CustomUser, related_name="participant_in_contests"
    )


class ContestRate(BaseAbstractModel, PermissionsMixin):
    rate = md.IntegerField(
        _("participant rate"),
        validators=[
            MinValueValidator(1, _("Value can't be less than 1")),
            MaxValueValidator(10, _("Value can't be bigger than 10")),
        ],
    )
    adjudicator = md.OneToOneField(CustomUser, on_delete=md.CASCADE)


class Story(BaseAbstractModel, PermissionsMixin):
    title = md.CharField(_("story title"), max_length=DbFieldsLength.CHAR_FIELD)
    author = md.ForeignKey(CustomUser, related_name=_("stories"), on_delete=md.CASCADE)
    rate = md.ForeignKey(
        ContestRate, related_name=_("adjudicator rate"), on_delete=md.CASCADE
    )
