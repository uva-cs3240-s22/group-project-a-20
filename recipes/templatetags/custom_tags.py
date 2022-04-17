from django import template

register = template.Library()

@register.simple_tag
def string_to_list(ingredients):
    return ingredients.split(",")