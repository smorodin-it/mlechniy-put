from rest_framework import serializers as sr

from contests.models.contests import Contest
from users.serializers import UserProfileSerializer


class ContestListSerializer(sr.ModelSerializer):
    class Meta:
        model = Contest
        fields = ["uuid", "title", "published", "start_date", "end_date"]


class ContestFullSerializer(sr.ModelSerializer):
    adjudicators = UserProfileSerializer(read_only=True, many=True)
    participants = UserProfileSerializer(read_only=True, many=True)

    class Meta:
        model = Contest
        exclude = ["id"]


class ContestCreateUpdateSerializer(sr.ModelSerializer):
    class Meta:
        model = Contest
        fields = ["title", "description", "start_date", "end_date"]


class ContestTogglePublishSerializer(sr.ModelSerializer):
    class Meta:
        model = Contest
        fields = ["published"]
