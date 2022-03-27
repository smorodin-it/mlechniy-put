from django.db.models import F
from django.http import HttpRequest
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from contests.models import Story, Contest
from mlechniy_put.utils.response_types import response_create, response_error
from users.forms import UserCreateForm
from users.models import UserProfile, CustomUser
from users.serializers import UserAdjudicatorCreateSerializer


def create_adjudicator_user(request):
    user_serializer = UserAdjudicatorCreateSerializer(data=request.data)
    if user_serializer.is_valid():
        profile_data = user_serializer.validated_data.pop("profile")
        profile = UserProfile(**profile_data)
        profile.save()
        adjudicator = CustomUser(**user_serializer.validated_data, profile=profile)
        adjudicator.user_type = CustomUser.ADJUDICATOR
        adjudicator.save()
        return response_create(adjudicator)
    return response_error(user_serializer.errors, 400)


def create_participant_user(request: HttpRequest):
    # Get active contest OR return error if no active contest
    now = timezone.now()
    active_published_contest = Contest.objects.filter(
        start_date__lt=now, end_date__gt=now, published=True
    ).first()
    if not active_published_contest:
        return response_error(_("No active contest found"), 404)

    user_form = UserCreateForm(request.POST, request.FILES)
    if user_form.is_valid():
        data = user_form.cleaned_data
        # Create User
        user = CustomUser()
        user.email = data["email"]
        # TODO: hash password!
        user.password = data["password"]

        # Create Profile
        profile = UserProfile()
        profile.first_name = data["first_name"]
        profile.last_name = data["last_name"]
        profile.patronymic = data["patronymic"]
        profile.phone = data["phone"]
        profile.age = data["age"]
        profile.post_address_author = data["post_address_author"]
        profile.edu_organization_name = data["edu_organization_name"]
        profile.edu_organization_address = data["edu_organization_address"]
        profile.teacher_full_name = data["teacher_full_name"]
        profile.teacher_position = data["teacher_position"]
        profile.save()

        # Link profile to user
        user.profile = profile
        user.save()

        # Add user to active contest
        active_published_contest.participants.add(user)
        active_published_contest.save()

        # Create Story
        story = Story()
        story.title = data["story_title"]
        # TODO: Implement file check
        story.file = request.FILES["story_file"]
        story.author = user
        story.contest = active_published_contest
        story.save()

        return response_create(user)

    return response_error(user_form.errors, 400)
