from django.shortcuts import render, redirect
from django.http import *

# Create your views here.

def get_days(request, day):
    return HttpResponse(f"It's {day}")

def todo_week(request, day):
    try:
        if day == 1:
            return HttpResponseRedirect('/week_days/todo_week/monday')
        elif day == 2:
            return redirect('/week_days/todo_week/tuesday')
        else:
            return HttpResponse('Error page')
    except Exception as ex:
        return HttpResponse(ex)