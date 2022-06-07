from rest_framework import serializers

from ..models import Box, User
from .user_serializers import UserSerializer


class BoxBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box


class BoxListSerializer(BoxBaseSerializer):
    class Meta(BoxBaseSerializer.Meta):
        fields = ("id", "title", "price_range", "manager")
        depth = 1


class BoxRetrieveSerializer(BoxBaseSerializer):
    class Meta(BoxBaseSerializer.Meta):
        fields = "__all__"
        depth = 1


class BoxCreateSerializer(BoxBaseSerializer):
    manager = UserSerializer()

    class Meta(BoxBaseSerializer.Meta):
        fields = (
            "title",
            "price_range",
            "last_join_data",
            "member_entry_message",
            "manager",
        )

    def create(self, validated_data):
        user = User.objects.create(**validated_data["manager"])
        validated_data["manager"] = user
        box = Box.objects.create(**validated_data)
        box.members.add(user)
        return box


class BoxUpdateSerializer(BoxBaseSerializer):
    class Meta(BoxBaseSerializer.Meta):
        exclude = ("manager", "members")


class BoxMemberJoinSerializer(UserSerializer):
    pass
