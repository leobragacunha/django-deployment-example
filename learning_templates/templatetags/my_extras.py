from django import template

register = template.Library()

# Custom filters

@register.filter(name='cut')
def cut(value, arg):
    """
    This function cuts all values of "arg" from the string
    """

    return value.replace(arg,'')

# register.filter('cut', cut)
