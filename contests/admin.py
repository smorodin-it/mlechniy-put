from django.contrib import admin
from django.contrib.admin import display
from django.utils.translation import gettext_lazy as _


# Register your models here.
from contests.models.contests import Contest
from contests.models.contest_rates import ContestRate
from contests.models.stories import Story


class StoryInline(admin.StackedInline):
    model = Story
    extra = 0
    verbose_name = _("story")
    verbose_name_plural = _("stories")


class ContestRateInline(admin.StackedInline):
    model = ContestRate
    extra = 0


class ContestAdmin(admin.ModelAdmin):
    model = Contest
    list_display = (
        "title",
        "published",
        "start_date",
        "end_date",
    )
    readonly_fields = ("uuid",)
    ordering = ("start_date",)
    inlines = [StoryInline]


class StoryAdmin(admin.ModelAdmin):
    model = Story
    readonly_fields = ("uuid",)
    inlines = [ContestRateInline]


class ContestRateAdmin(admin.ModelAdmin):
    model = ContestRate
    readonly_fields = ("uuid",)
    list_display = ("story", "rate", "get_adjudicator")

    @display(ordering="adjudicator__profile__first_name", description=_("adjudicator"))
    def get_adjudicator(self, obj: ContestRate) -> str:
        return obj.adjudicator.profile.get_short_name()


admin.site.register(Contest, ContestAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(ContestRate, ContestRateAdmin)
