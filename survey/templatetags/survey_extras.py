from django import template
import random


register = template.Library()

@register.filter
def get_surveys(value):
    """
        Returns the correct list of surveys whether the input is a Paginator page
        or a plain list/queryset.
    """
    # If it's a paginator page object 
    # like page.object_list
    if hasattr(value, "object_list"):
        """
        If the value has an attribute 'object_list', it's likely a Paginator page.
        We return that list of objects.
        """
        return value.object_list
    # If it's already a list or queryset
    return value

@register.filter
def shuffle_if(seq, condition):
    """Shuffle if condition is True, otherwise return original"""
    if condition:
        try:
            result = list(seq)[:] 
            random.shuffle(result)
            return result
        except:
            return seq
    return seq

@register.filter()
def get_range(min_val, max_val):
    """
    Returns a range of numbers from min to max.
    Usage: {% for i in 1|get_range:5 %}
    """
    try:
        min_val = int(min_val)
        max_val = int(max_val)
        return range(min_val, max_val + 1)
    except (ValueError, TypeError):
        return []