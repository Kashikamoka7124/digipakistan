
from django.contrib import admin
from django.urls import path
from superadmin.views import *
from superadmin import views

from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
      
    # path('forget', views.forget, name = "forget"),
    # path('reset', views.reset, name = "reset"),
    # path('portal', views.portal , name = "portal"),
    # path('', views.home, name = "home"),
    # path('log_in', views.login_page , name = "login_page"),
    # path('log_out', views.logout_page , name = "logout_page"),
    # path('Assignment', views.assignment, name = "assignmnet_page"),

    path('profile', views.ProfileView.as_view() , name = "profile"),
]