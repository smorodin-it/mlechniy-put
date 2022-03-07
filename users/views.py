from rest_framework import generics as gen

from users.models import CustomUser
from users.serializers import (
    UserListSerializer,
    UserParticipantUpdateProfileSerializer,
)
from users.utils import create_user


class UserUpdateDestroyView(gen.UpdateAPIView, gen.DestroyAPIView):
    """
    Only admin can interact with this view
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserParticipantUpdateProfileSerializer


class ParticipantListView(gen.ListAPIView):
    """
    Only staff can interact with this view
    """

    serializer_class = UserListSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(user_type=CustomUser.PARTICIPANT)


class ParticipantInActiveContestListView(gen.ListAPIView):
    """
    TODO: Implement after Contest implementation!
    Нужно уточнить кто может видеть этих пользователей.
    Кто может видеть:
    - Админ;
    - Жюри;
    - Участники конкурса?
    """

    pass


class ParticipantCreateView(gen.CreateAPIView):
    """
    TODO: implement file check and upload here
    """

    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        return create_user(request, CustomUser.PARTICIPANT, *args, **kwargs)


class AdjudicatorCreateView(gen.CreateAPIView):
    """
    can create by anonymous user
    """

    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        return create_user(request, CustomUser.ADJUDICATOR, *args, **kwargs)


class AdjudicatorListView(gen.ListAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(user_type=CustomUser.ADJUDICATOR)
