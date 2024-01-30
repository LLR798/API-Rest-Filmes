from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_movies, name='get_all_movies'),
    path('movie/<int:id>', views.get_by_id),
    path('data/', views.movie_manager),
    path('data/<int:id>/delete/', views.delete_movie),
]