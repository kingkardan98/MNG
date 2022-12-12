from django import template

register = template.Library()

@register.filter(name='intoSpace')
def intoSpace(value, arg):
    return value.replace(arg, ' ')