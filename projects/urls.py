from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_projects, name='projects'),
    path('add', views.create_project, name='add'),
    path('add-form', views.create_project_form, name='add-form'),
    path('edit/<int:id>', views.edit_project, name='edit'),
    path('delete/<slug:id>', views.delete_project, name='delete'),
]
