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

from users import urls as users_urls
from contests import urls as contests_urls

urlpatterns = [
    # Admin site
    path("admin/", admin.site.urls),
    # API
    path(
        "api/v1/",
        include(
            [
                # Users
                path("user/", include(users_urls)),
                # Contest
                path("contest/", include(contests_urls)),
            ]
        ),
    ),
]
