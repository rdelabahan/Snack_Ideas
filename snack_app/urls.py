from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_idea', views.create_idea),
    path('<int:idea_id>', views.display_idea),
    path('<int:idea_id>/like', views.like),
    path('<int:idea_id>/dislike', views.dislike),
    path('<int:idea_id>/delete', views.delete),
]