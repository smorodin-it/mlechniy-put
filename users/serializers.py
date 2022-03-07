from rest_framework import serializers as sr

from users.models import CustomUser, UserProfile


class UserProfileSerializer(sr.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name", "patronymic"]


class UserFullProfileSerializer(sr.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = "__all__"


class UserCreateUpdateProfileSerializer(sr.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ["id", "created_at", "updated_at"]


class UserListSerializer(sr.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ["uuid", "profile"]


class UserParticipantCreateSerializer(sr.ModelSerializer):
    """
    TODO: Need re-implement with form and file upload \n
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


class UserAdjudicatorCreateSerializer(sr.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = CustomUser
        fields = ["email", "password", "profile"]
