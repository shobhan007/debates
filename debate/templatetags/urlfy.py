from urllib import quote_plus
from django import template

register=template.Library()

@register.filter
def urlfy(value):
    return quote_plus(value)