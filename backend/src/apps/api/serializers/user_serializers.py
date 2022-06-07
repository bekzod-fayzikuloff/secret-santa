from rest_framework import serializers

from ..models import Box, User


class BoxListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ("id", "title", "price_range", "manager")
        depth = 1


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = "__all__"


class UserRetrieveSerializer(BaseUserSerializer):
    box = serializers.SerializerMethodField()

    @staticmethod
    def get_box(user):
        return BoxListSerializer(Box.objects.get(members__exact=user)).data

    class Meta(BaseUserSerializer.Meta):
        fields = ("first_name", "last_name", "email", "box")
