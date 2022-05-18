from django.db import models
from django.utils import timezone

from ..core.mixins import AbstractUUID


class User(AbstractUUID):
    first_name = models.CharField(max_length=120, blank=False, null=False)
    last_name = models.CharField(max_length=120, blank=False, null=False)
    email = models.EmailField(max_length=120)

    def __str__(self) -> str:
        return f"{self.email} -> {self.first_name}"

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


class Box(AbstractUUID):
    class GameState(models.TextChoices):
        OPEN = ("OP", "Open")
        DURING = ("DU", "During")
        COMPLETED = ("CO", "Completed")

    title = models.CharField(max_length=255)
    price_range = models.PositiveIntegerField()
    last_join_data = models.DateField()
    member_entry_message = models.TextField(max_length=2000)
    box_state = models.CharField(
        max_length=2,
        choices=GameState.choices,
        default=GameState.OPEN,
    )
    manager = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="boxes",
    )
    members = models.ManyToManyField(User, related_name="box")

    def __str__(self) -> str:
        return f"{self.title} -> {self.manager.first_name}"

    class Meta:
        verbose_name = "box"
        verbose_name_plural = "boxes"


class TossResult(AbstractUUID):
    box = models.ForeignKey(
        Box,
        on_delete=models.CASCADE,
    )
    get_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_from")
    present_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="present_to")

    def __str__(self) -> str:
        return f"{self.get_from} <-> {self.present_to}"

    class Meta:
        verbose_name = "toss"
        verbose_name_plural = "tosses"


class Questionary(models.Model):
    maker = models.ForeignKey(User, on_delete=models.CASCADE)
    to_box = models.ForeignKey(Box, on_delete=models.CASCADE, related_name="questionary")
    content = models.TextField(max_length=1000)

    def __str__(self) -> str:
        return f"{self.maker.email} -> {self.to_box.title}"

    class Meta:
        verbose_name = "questionary"
        verbose_name_plural = "questionaries"


class SecretChat(models.Model):
    to_box = models.ForeignKey(Box, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.to_box}"

    class Meta:
        verbose_name = "secret_chat"
        verbose_name_plural = "secret_chats"


class Message(models.Model):
    to_chat = models.ForeignKey(SecretChat, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    message_from = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.message_from} -> {self.to_chat}"

    class Meta:
        verbose_name = "message"
        verbose_name_plural = "messages"
