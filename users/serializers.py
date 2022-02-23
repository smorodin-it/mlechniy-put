from rest_framework import serializers as sr

from users.models import CustomUser, UserProfile


class UserProfileSerializer(sr.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'patronymic']


class UserFullProfileSerializer(sr.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['__all__']


class UserListSerializer(sr.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['uuid', 'profile']


class UserParticipantCreateSerializer(sr.ModelSerializer):
    """
    TODO: Need re-implement with form and file upload \n
    TODO: Need implement confirm password field and check it!
    """

    profile = UserFullProfileSerializer()

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'profile']


class UserParticipantUpdateProfileSerializer(sr.ModelSerializer):
    profile = UserFullProfileSerializer()

    class Meta:
        model = CustomUser
        fields = ['profile']
