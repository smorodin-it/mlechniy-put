from rest_framework import serializers as sr

from contests.models import Story
from users.serializers import UserProfileSerializer


class StoryListSerializer(sr.ModelSerializer):
    author = sr.SerializerMethodField("get_author")

    def get_author(self, obj: Story):
        return {
            "uuid": obj.author.uuid,
            "first_name": obj.author.profile.first_name,
            "last_name": obj.author.profile.last_name,
            "patronymic": obj.author.profile.patronymic,
            "short_name": obj.author.profile.get_short_name(),
        }

    class Meta:
        model = Story
        fields = ["uuid", "title", "author"]
