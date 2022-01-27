from django import template

register = template.Library()

@register.filter()
def put_sport(value, arg):
    if arg == "SPORT":
        if value.category == 25:
            return value
        else:
            return ""
    return ""
