from django.urls import path
from django.http import HttpResponse
from django.template.loader import render_to_string
from . import views

def main(request):
    return HttpResponse('Главная страница')

def posts(request, info):
    try:
        return HttpResponse(f'Информация о блоге {info}')
    except Exception as ex:
        return HttpResponse(ex)
def posts_number(request, info):
    try:
        return HttpResponse(f'Номер блога {info}')
    except Exception as ex:
        return HttpResponse(ex)
def all_post(request):
    return HttpResponse(render_to_string('blog/index.html'))