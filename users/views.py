from djangorestframework_camel_case.parser import CamelCaseMultiPartParser
from rest_framework import generics as gen
from rest_framework_simplejwt.views import TokenObtainPairView

from mlechniy_put.utils.create_user import (
    create_adjudicator_user,
    create_participant_user,
)
from users.models import CustomUser
from users.serializers import (
    UserListSerializer,
    UserParticipantUpdateProfileSerializer,
    UserRetrieveSerializer, CustomTokenObtainSerializer,
)


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
    queryset = CustomUser.objects.all()
    parser_classes = [CamelCaseMultiPartParser]

    def post(self, request, *args, **kwargs):
        return create_participant_user(request)


class AdjudicatorCreateView(gen.CreateAPIView):
    """
    can create by anonymous user
    """

    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        return create_adjudicator_user(request)


class AdjudicatorListView(gen.ListAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(user_type=CustomUser.ADJUDICATOR)


class UserRetrieveView(gen.RetrieveAPIView):
    # TODO: Set special permissions to only see self data (or get user by uuid from )
    queryset = CustomUser.objects.all()
    serializer_class = UserRetrieveSerializer
    lookup_field = "uuid"


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer
