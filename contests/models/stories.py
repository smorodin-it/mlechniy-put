from uuid import uuid4

from django.db import models as md
from django.utils.translation import gettext_lazy as _

from mlechniy_put.constants import DbFieldsLength
from mlechniy_put.models import BaseAbstractModel
from users.models import CustomUser


class Story(BaseAbstractModel):
    uuid = md.UUIDField(default=uuid4, editable=False, unique=True)
    title = md.CharField(_("story title"), max_length=DbFieldsLength.CHAR_FIELD)
    author = md.ForeignKey(CustomUser, related_name="stories", on_delete=md.CASCADE)
    contest = md.ForeignKey(
        "Contest",
        on_delete=md.CASCADE,
        related_name="stories",
        null=True,
    )

    def __str__(self):
        return f"{self.author.profile.get_short_name()} - {self.title}"
