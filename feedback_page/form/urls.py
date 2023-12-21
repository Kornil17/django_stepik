from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('form', FeedbackView.as_view()),
    path('done', DoneView.as_view()),
    path('<int:id_feedback>', UpdateView.as_view()),
    path('list', ListFeedBack.as_view()),
    path('detail/<pk>', DetailFeedBack.as_view())
]