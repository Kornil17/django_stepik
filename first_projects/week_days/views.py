from django.shortcuts import render, redirect
from django.http import *
from django.urls import reverse

# Create your views here.

def get_days(request, day):
    return HttpResponse(f"It's {day}")

def todo_week(request, day):
    try:
        days = {1:'monday', 2:'tuesday'}
        if day == 1:
            week_days = reverse('str_week', args=('monday',))
            return HttpResponseRedirect(week_days)
        elif day == 2:
            week_days = reverse('str_week', args=('tuesday',))
            return HttpResponseRedirect(week_days)
        else:
            return HttpResponse('Error page')
    except Exception as ex:
        return HttpResponse(ex)