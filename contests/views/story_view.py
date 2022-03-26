from rest_framework import generics as gen

from contests.models import Story
from contests.serializers.story_serializer import (
    StoryListSerializer,
    StoryRetrieveSerializer,
)


class StoryListView(gen.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryListSerializer


class StoryRetrieveView(gen.RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryRetrieveSerializer
    lookup_field = "uuid"
