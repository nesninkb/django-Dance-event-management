# danceapp/templatetags/extra_filters.py

from django import template

register = template.Library()


@register.filter
def dict_lookup(d, key):
    """
    Allows dictionary lookup in Django templates
    Usage: {{ mydict|dict_lookup:key }}
    """
    if isinstance(d, dict):
        return d.get(key)
    return None


@register.filter
def gender_symbol(value):
    """
    Converts gender code to symbol
    """
    if value == 'M':
        return 'Male ♂'
    if value == 'F':
        return 'Female ♀'
    return ''
