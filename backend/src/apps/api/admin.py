from django.contrib import admin

from .models import Box, Message, Questionary, SecretChat, TossResult, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ("email",)
    list_display = ("first_name", "last_name")
    list_display_links = ("first_name", "last_name")
    search_fields = ["email", "first_name"]


@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_filter = ("box_state",)
    list_display = ("title", "manager")
    list_display_links = ("title",)
    search_fields = ("title", "manager__first_name", "manager__email")


@admin.register(TossResult)
class TossResultAdmin(admin.ModelAdmin):
    list_display = ("box", "get_from", "present_to")
    list_display_links = ("box",)
    search_fields = (
        "box__title",
        "get_from__email",
        "get__from_first_name" "present_to__email",
        "present_to__first_name",
    )


@admin.register(Questionary)
class QuestionaryAdmin(admin.ModelAdmin):
    list_display = ("id", "maker", "to_box")
    list_display_links = ("maker", "to_box")
    search_fields = ("to_box__title", "maker__email")


@admin.register(SecretChat)
class SecretChatAdmin(admin.ModelAdmin):
    list_display = ("to_box",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
