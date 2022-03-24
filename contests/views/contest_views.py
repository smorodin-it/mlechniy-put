from rest_framework import generics as gen

from contests.models.contests import Contest
from contests.serializers.contest_serializer import (
    ContestListSerializer,
    ContestCreateUpdateSerializer,
    ContestFullSerializer,
    ContestTogglePublishSerializer,
)


class ContestListView(gen.ListAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestListSerializer


class ContestCreateView(gen.CreateAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestCreateUpdateSerializer
    # TODO: Add all active adjudicators to new contest by default


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
