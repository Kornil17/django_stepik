from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

signs = ['aquarius', 'gemini', 'libra', 'scorpio', 'capricorn', 'leo']
elements = ['air', 'fire', 'earth', 'water']
sign_list = {"air": ['gemini'], "fire": ['libra', 'capricorn'], "earth": ['scorpio', 'leo'], "water": ['aquarius']}


def sign(request):
    return render(request, 'horoscope/menu.html', {'signs':signs})

def type(request):
    return render(request, 'horoscope/type.html', {'elements':elements})
def sign_type(request, type):
    return render(request, 'horoscope/sign_type.html', {'sign_list':sign_list, 'sign_type':type})

def number(request, number):
    return HttpResponse(f'We get number={number} from own converter int5')

def float_number(request, number):
    return HttpResponse(f'We get number={number} from own converter float_number')

def get_sign(request, sign_zodiak):
    return render(request, 'horoscope/information_sign.html', {'sign_zodiak': sign_zodiak})


# def index(request):
#     url = 'get_sign'
#     return HttpResponse(formed_list(signs, url))

# def types(request):
#     url = 'sign_types'
#     return HttpResponse(formed_list(elements, url))
#
#
# def formed_list(parametrs, url):
#     lists = ''
#     for i in parametrs:
#         uri = reverse(url, args=(i,))
#         lists += f"<li><a href='{uri}'>{i.title()}</a></li>"
#     result = f'<ul>{lists}</ul>'
#     return result
#
#
# def sign_types(request, type):
#     types = {"air": ['gemini'], "fire": ['libra', 'capricorn'], "earth": ['scorpio', 'leo'], "water": ['aquarius']}
#     lists = ''
#     for i in types[type]:
#         lists += f"<li>{i.title()}</li>"
#     result = f'<ul>{lists}</ul>'
#     return HttpResponse(result)

