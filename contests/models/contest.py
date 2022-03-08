from uuid import uuid4

from django.db import models as md
from django.utils.translation import gettext_lazy as _

from mlechniy_put.constants import DbFieldsLength
from mlechniy_put.models import BaseAbstractModel
from users.models import CustomUser


class Contest(BaseAbstractModel):
    uuid = md.UUIDField(default=uuid4, editable=False, unique=True)
    title = md.CharField(_("contest title"), max_length=DbFieldsLength.CHAR_FIELD)
    description = md.TextField(
        _("contest description"),
        max_length=DbFieldsLength.TEXT_FIELD,
        null=True,
        blank=True,
    )
    start_date = md.DateField(_("contest start date"))
    end_date = md.DateField(_("contest end date"))
    published = md.BooleanField(_("published"), default=False)
    adjudicators = md.ManyToManyField(
        CustomUser, related_name="adjudicator_in_contests"
    )
    participants = md.ManyToManyField(
        CustomUser, related_name="participant_in_contests"
    )

    def __str__(self):
        return f"{self.title} - {self.start_date} - {self.end_date}"

    def is_active(self) -> bool:
        """
        Check if current contest can get participant stories
        :return:
        """
        pass
