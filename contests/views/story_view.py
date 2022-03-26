from rest_framework import generics as gen

from contests.models import Story
from contests.serializers.story_serializer import StoryListSerializer


class StoryListView(gen.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryListSerializer
