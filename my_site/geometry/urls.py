from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:hight>', views.get_rectangle_area),
    path('square/<int:width>', views.get_square_area),
    path('circle/<int:radius>', views.get_circle_area),
    path('get_rectangle_area/<int:width>/<int:height>', views.redirect_rectangle),
    path('get_square_area/<int:width>', views.redirect_square),
    path('get_circle_area/<int:radius>', views.redirect_circle),

]

