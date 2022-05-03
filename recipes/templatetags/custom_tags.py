from django import template

register = template.Library()

@register.simple_tag
def string_to_list(ingredients):
    #got an error where a NoneType gets passed in and breaks this, this fixed it but if it causes chaos down the line that was my reasoning at least lol
    if(ingredients):
        return ingredients.split(";")
    return []