from django.contrib import admin

# Register your models here.
from contests.models.contest import Contest
from contests.models.contest_rate import ContestRate
from contests.models.story import Story

admin.site.register(Contest)
admin.site.register(ContestRate)
admin.site.register(Story)
