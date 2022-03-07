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
