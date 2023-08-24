from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_users),
    path('<slug:id>', views.get_user_by_id),
]
