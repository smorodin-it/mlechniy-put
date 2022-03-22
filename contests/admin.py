from django.contrib import admin

# Register your models here.
from contests.models.contests import Contest
from contests.models.contest_rates import ContestRate
from contests.models.stories import Story

admin.site.register(Contest)
admin.site.register(ContestRate)
admin.site.register(Story)
