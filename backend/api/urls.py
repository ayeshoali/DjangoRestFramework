from django import views
from django.urls import path

from . import views


urlpatterns = [
  path('', views.api_home.as_view()),
    
]
