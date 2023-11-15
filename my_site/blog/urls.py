from django.urls import path
from . import views

urlpatterns = [
    path('posts/<int:info>', views.posts_number),
    path('posts/<str:info>', views.posts),
]