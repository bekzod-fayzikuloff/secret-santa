from rest_framework import serializers

from ..models import TossResult


class TossResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TossResult
        fields = "__all__"
