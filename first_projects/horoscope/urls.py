from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FifthItnConverter, "int5")
register_converter(converters.FloatConverter, "float_number")


urlpatterns = [
    path('', views.sign),
    path('<int5:number>', views.number, name='number'),
    path('<float_number:number>', views.float_number, name='float_number'),
    path('type', views.type, name='types'),
    path('type/<type>', views.sign_type, name='type'),
    path('<sign_zodiak>', views.get_sign, name='get_sign'),
]
