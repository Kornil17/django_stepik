from django.urls import path
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import redirect, render
from . import views

def main(request):
    return HttpResponse('Главная страница')

def posts(request, info):
    try:
        # return HttpResponse(f'Информация о блоге {info}')
        return render(request, 'blog/detail_by_name.html', {'name':info})
    except Exception as ex:
        return HttpResponse(ex)
def posts_number(request, info):
    try:
        # return HttpResponse(f'Номер блога {info}')
        return render(request, 'blog/detail_by_number.html', {'number':info})
    except Exception as ex:
        return HttpResponse(ex)
def all_post(request):
    return HttpResponse(render_to_string('blog/index.html'))