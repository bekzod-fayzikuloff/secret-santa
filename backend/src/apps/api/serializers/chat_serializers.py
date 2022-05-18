from rest_framework import serializers

from ..models import Message, SecretChat


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message


class RetrieveMessageSerializer(MessageSerializer):
    class Meta(MessageSerializer.Meta):
        fields = ("id", "content", "created_at")


class CreateMessageSerializer(MessageSerializer):
    class Meta(MessageSerializer.Meta):
        fields = ("content",)


class ChatSerializer(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField()

    @staticmethod
    def get_messages(chat: SecretChat):
        messages = Message.objects.filter(to_chat=chat)

        return RetrieveMessageSerializer(messages, many=True).data

    class Meta:
        model = SecretChat
        fields = ("to_box", "messages")
