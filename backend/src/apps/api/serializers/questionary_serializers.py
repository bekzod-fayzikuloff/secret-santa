from rest_framework import serializers

from ..models import Questionary, User
from .user_serializers import UserSerializer


class QuestionaryUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ("first_name", "last_name", "email")


class BaseQuestionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionary


class ListQuestionarySerializer(BaseQuestionarySerializer):
    maker = QuestionaryUserSerializer()

    class Meta(BaseQuestionarySerializer.Meta):
        fields = ("id", "content", "maker")

    def create(self, validated_data):
        maker = User.objects.create(**validated_data["maker"])
        validated_data["maker"] = maker
        return Questionary.objects.create(**validated_data)


class UpdateQuestionarySerializer(BaseQuestionarySerializer):
    class Meta(BaseQuestionarySerializer.Meta):
        fields = ("content",)
