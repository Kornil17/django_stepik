from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()

@register.filter(name='split')
@stringfilter
def split(value, key=' '):
    return value.split(key)

@register.filter(name='circle')
def cicrle(n: int=1):
    return range(1, n+1)