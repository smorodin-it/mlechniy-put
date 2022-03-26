from django.urls import path

from contests.views.contest_views import (
    ContestListView,
    ContestCreateView,
    ContestUpdateDestroyView,
    ContestRetrieveView,
    ContestTogglePublish,
)
from contests.views.story_view import StoryListView, StoryRetrieveView

contest_urlpatterns = [
    # Base CRUD
    path("list/", ContestListView.as_view()),
    path("create/", ContestCreateView.as_view()),
    path("retrieve/<str:uuid>/", ContestRetrieveView.as_view()),
    path("update/<str:uuid>/", ContestUpdateDestroyView.as_view()),
    path("delete/<str:uuid>/", ContestUpdateDestroyView.as_view()),
    # Toggle publish
    path("toggle-publish/<str:uuid>/", ContestTogglePublish.as_view()),
]

story_urlpatterns = [
    # Base CRUD
    path("list/", StoryListView.as_view()),
    path("retrieve/<str:uuid>", StoryRetrieveView.as_view()),
    # path("create/", ContestCreateView.as_view()),
    # path("retrieve/<str:uuid>/", ContestRetrieveView.as_view()),
    # path("update/<str:uuid>/", ContestUpdateDestroyView.as_view()),
    # path("delete/<str:uuid>/", ContestUpdateDestroyView.as_view()),
    # Toggle publish
    # path("toggle-publish/<str:uuid>/", ContestTogglePublish.as_view()),
]
