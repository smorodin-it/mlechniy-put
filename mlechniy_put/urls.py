"""mlechniy_put URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from frontend import views as frontend_views
from users import urls as users_urls
from contests.urls import contest_urlpatterns, story_urlpatterns
from users.views import CustomTokenObtainPairView

urlpatterns = [
    # Admin site
    path("admin/", admin.site.urls),
    # Participant site
    path("", frontend_views.participant_view, name="index"),
    # Adjudicator site
    # API
    path(
        "api/v1/",
        include(
            [
                # Auth
                path("auth/token/", CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
                path("auth/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
                # Users
                path("user/", include(users_urls)),
                # Contest
                path("contest/", include(contest_urlpatterns)),
                # Contest
                path("story/", include(story_urlpatterns)),
            ]
        ),
    ),
]
