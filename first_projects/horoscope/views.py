from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

signs = ['aquarius', 'gemini', 'libra', 'scorpio', 'capricorn', 'leo']
elements = ['air', 'fire', 'earth', 'water']


def index(request):
    url = 'get_sign'
    return HttpResponse(formed_list(signs, url))

def number(request, number):
    return HttpResponse(f'We get number={number} from own converter int5')

def float_number(request, number):
    return HttpResponse(f'We get number={number} from own converter float_number')
def types(request):
    url = 'sign_types'
    return HttpResponse(formed_list(elements, url))


def formed_list(parametrs, url):
    lists = ''
    for i in parametrs:
        uri = reverse(url, args=(i,))
        lists += f"<li><a href='{uri}'>{i.title()}</a></li>"
    result = f'<ul>{lists}</ul>'
    return result


def sign_types(request, sign_type):
    types = {"air": ['gemini'], "fire": ['libra', 'capricorn'], "earth": ['scorpio', 'leo'], "water": ['aquarius']}
    lists = ''
    for i in types[sign_type]:
        lists += f"<li>{i.title()}</li>"
    result = f'<ul>{lists}</ul>'
    return HttpResponse(result)


def get_sign(request, sign_zodiak):
    response = render_to_string('horoscope/signs.html')
    return HttpResponse(response)
