from django.db import models as md


class BaseAbstractModel(md.Model):
    created_at = md.DateTimeField(auto_now_add=True)
    updated_at = md.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
