import base64

from django.core.files import File
from rest_framework import serializers as sr

from contests.models import Story


def create_author_dict(obj: Story) -> dict:
    return {
        "uuid": obj.author.uuid,
        "first_name": obj.author.profile.first_name,
        "last_name": obj.author.profile.last_name,
        "patronymic": obj.author.profile.patronymic,
        "short_name": obj.author.profile.get_short_name(),
    }


class StoryListSerializer(sr.ModelSerializer):
    author = sr.SerializerMethodField("get_author")

    def get_author(self, obj: Story) -> dict:
        return create_author_dict(obj)

    class Meta:
        model = Story
        fields = ["uuid", "title", "author"]


class StoryRetrieveSerializer(sr.ModelSerializer):
    author = sr.SerializerMethodField("get_author")

    def get_author(self, obj: Story) -> dict:
        return create_author_dict(obj)

    class Meta:
        model = Story
        fields = ["uuid", "title", "author"]

    def to_representation(self, instance: Meta.model):
        ret = super().to_representation(instance)
        file: File = instance.file.file
        file_base64 = base64.encodebytes(file.read())
        ret["story_file"] = str(file_base64)
        return ret
