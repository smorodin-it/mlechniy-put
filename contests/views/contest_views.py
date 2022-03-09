from rest_framework import generics as gen
from rest_framework.renderers import JSONRenderer

from contests.models.contest import Contest
from contests.serializers.contest_serializer import (
    ContestListSerializer,
    ContestCreateUpdateSerializer,
    ContestFullSerializer,
    ContestTogglePublishSerializer,
)


class ContestListView(gen.ListAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestListSerializer
    renderer_classes = JSONRenderer


class ContestCreateView(gen.CreateAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestCreateUpdateSerializer


class ContestUpdateDestroyView(gen.UpdateAPIView, gen.DestroyAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestCreateUpdateSerializer
    lookup_field = "uuid"


class ContestRetrieveView(gen.RetrieveAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestFullSerializer
    lookup_field = "uuid"


class ContestTogglePublish(gen.UpdateAPIView):
    queryset = Contest.objects.all()
    lookup_field = "uuid"
    serializer_class = ContestTogglePublishSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
