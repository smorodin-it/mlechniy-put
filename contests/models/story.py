from django.contrib.auth.models import PermissionsMixin
from django.db import models as md
from django.utils.translation import gettext_lazy as _

from contests.models.contest_rate import ContestRate
from mlechniy_put.constants import DbFieldsLength
from mlechniy_put.models import BaseAbstractModel
from users.models import CustomUser


class Story(BaseAbstractModel, PermissionsMixin):
    title = md.CharField(_("story title"), max_length=DbFieldsLength.CHAR_FIELD)
    author = md.ForeignKey(CustomUser, related_name=_("stories"), on_delete=md.CASCADE)
    rate = md.ForeignKey(
        ContestRate, related_name=_("adjudicator rate"), on_delete=md.CASCADE
    )
