from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from math import pi

def get_rectangle_area(request, width, hight):
    # return HttpResponse(f'{width * hight}')
    return render(request, 'geometry/rectangle.html', {'square': width*hight})

def get_square_area(request, width):
    # return HttpResponse(f'{width ** 2}')
    return render(request, 'geometry/square.html', {'square': width**2})

def get_circle_area(request, radius):
    # return HttpResponse(f'{pi * radius**2}')
    return render(request, 'geometry/circle.html', {'square': pi * radius**2})

def redirect_rectangle(request, width, height):
    return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}')

def redirect_square(request, width):
     return HttpResponseRedirect(f'/calculate_geometry/square/{width}')

def redirect_circle(request, radius):
    return redirect(f'/calculate_geometry/circle/{radius}')
