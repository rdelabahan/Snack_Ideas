from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.authenticate_user),
    path('logout', views.logout),
    path('users/<int:user_id>', views.display_profile),
    path('users/<int:user_id>/update', views.update_profile),
]