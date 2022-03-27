from rest_framework import serializers as sr

from users.models import CustomUser, UserProfile


class UserProfileSerializer(sr.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name", "patronymic"]


class UserFullProfileSerializer(sr.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ["id"]


class UserCreateUpdateProfileSerializer(sr.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ["id", "created_at", "updated_at"]


class UserListSerializer(sr.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ["uuid", "profile"]


class UserAdjudicatorCreateSerializer(sr.ModelSerializer):
    """
    TODO: Need implement confirm password field and check it!
    """

    profile = UserCreateUpdateProfileSerializer()

    class Meta:
        model = CustomUser
        fields = ["email", "password", "profile"]


class UserParticipantUpdateProfileSerializer(sr.ModelSerializer):
    profile = UserCreateUpdateProfileSerializer()

    class Meta:
        model = CustomUser
        fields = ["profile"]


class UserRetrieveSerializer(sr.ModelSerializer):
    profile = UserFullProfileSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ["email", "uuid", "profile"]
