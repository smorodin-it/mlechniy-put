from rest_framework import serializers as sr

from contests.models.contest import Contest


class ContestListSerializer(sr.ModelSerializer):
    class Meta:
        model = Contest
        fields = ["uuid", "title", "published", "start_date", "end_date"]


class ContestFullSerializer(sr.ModelSerializer):
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
