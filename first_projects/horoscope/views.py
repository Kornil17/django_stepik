from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def get_sign(request, sign_zodiak):
    return HttpResponse(f"It's the {sign_zodiak} horoscope")



