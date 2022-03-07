from django.urls import path

from users.views import (
    ParticipantCreateView,
    AdjudicatorListView,
    AdjudicatorCreateView,
    ParticipantListView,
    ParticipantInActiveContestListView,
    UserRetrieveView,
)

urlpatterns = [
    # Participants
    path("participant/", ParticipantCreateView.as_view()),
    path("participant/", ParticipantListView.as_view()),
    # TODO: enable after implementation
    # path(
    #     "participant/active-contest-list/", ParticipantInActiveContestListView.as_view()
    # ),
    # Adjudicators
    path("adjudicator-create/", AdjudicatorCreateView.as_view()),
    path("adjudicator-list/", AdjudicatorListView.as_view()),
    # Users
    path("<str:uuid>/", UserRetrieveView.as_view()),
]
