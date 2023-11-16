from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FifthItnConverter, "int5")
register_converter(converters.FloatConverter, "float_number")


urlpatterns = [
    path('', views.index),
    path('<int5:number>', views.number, name='number'),
    path('<float_number:number>', views.float_number, name='float_number'),
    path('type', views.types, name='types'),
    path('type/<sign_type>', views.sign_types, name='sign_types'),
    path('<sign_zodiak>', views.get_sign, name='get_sign'),
]
