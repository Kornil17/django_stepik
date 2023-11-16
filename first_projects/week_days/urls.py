from django.urls import path
from . import views

urlpatterns = [
    path('todo_week/<int:day>', views.todo_week, name='int_week'),
    path('todo_week/<day>', views.get_days, name='str_week'),
]
