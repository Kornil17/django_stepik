from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_films, name='list_films'),
    path('<slug:slug_movie>', views.movie, name='movie'),
    path('authors/', views.authors, name='authors'),
    path('authors/<str:name>', views.author, name='author')
]