# Users/templatetags/custom_filters.py
from django import template

register = template.Library()


@register.filter(name="add_attrs")
def add_attrs(field, attrs):
    attrs = dict(attr.split("=") for attr in attrs.split(","))
    return field.as_widget(attrs=attrs)
