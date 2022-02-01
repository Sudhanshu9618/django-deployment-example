from django import template


register = template.Library()


def cut(value, arg):
    """
    this cut aii values "arg" from the string
    """

    return value.replace(arg, '')


register.filter('cut', cut),
