from django.contrib import admin

from users.models import UserProfile, CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser

    list_display = (
        "email",
        "profile",
        "user_type",
        "is_staff",
        "is_active",
    )
    list_filter = ("is_staff", "is_active", "user_type")
    readonly_fields = ["uuid", "password", "created_at", "updated_at", "last_login"]

    search_fields = ("email", "profile__first_name", "profile__last_name")
    ordering = ("profile",)


admin.site.register(CustomUser, CustomUserAdmin)
# TODO: Implement custom profile admin model with user readonly field
admin.site.register(UserProfile)
