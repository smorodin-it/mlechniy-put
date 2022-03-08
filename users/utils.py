from rest_framework.response import Response

from mlechniy_put.utils import response_create, response_error
from users.models import UserProfile, CustomUser
from users.serializers import UserParticipantCreateSerializer


def create_user(request, user_type, *args, **kwargs):
    user_serializer = UserParticipantCreateSerializer(data=request.data)
    if user_serializer.is_valid():
        profile_data = user_serializer.validated_data.pop("profile")
        profile = UserProfile(**profile_data)
        profile.save()
        participant = CustomUser(**user_serializer.validated_data, profile=profile)
        participant.user_type = user_type
        participant.save()
        return response_create(participant)
    return response_error(user_serializer.errors, 400)
