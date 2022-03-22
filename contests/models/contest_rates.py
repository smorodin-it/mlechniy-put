from uuid import uuid4

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models as md
from django.utils.translation import gettext_lazy as _

from mlechniy_put.models import BaseAbstractModel
from users.models import CustomUser


class ContestRate(BaseAbstractModel):
    uuid = md.UUIDField(default=uuid4, editable=False, unique=True)
    rate = md.IntegerField(
        _("participant rate"),
        validators=[
            MinValueValidator(1, _("Value can't be less than 1")),
            MaxValueValidator(10, _("Value can't be bigger than 10")),
        ],
    )
    adjudicator = md.OneToOneField(CustomUser, on_delete=md.CASCADE)
    story = md.OneToOneField("Story", on_delete=md.CASCADE)
