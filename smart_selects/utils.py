# -*- coding: utf-8 -*-
import django
from django.apps import apps
from django.utils.encoding import force_text
import unicodedata
import string

get_model = apps.get_model

def unicode_sorter(data):
    """ This function implements sort keys for the all language."""
    return ''.join(x for x in unicodedata.normalize('NFKD', data) if x in string.ascii_letters).lower()


def get_limit_choices_to(app_name, model_name, field_name):
    try:
        model = get_model(app_name, model_name)
        field = model._meta.get_field(field_name)
        limit_choices_to = (field.rel.limit_choices_to
                            if django.VERSION < (2, 0)
                            else field.remote_field.limit_choices_to)
    except Exception:
        limit_choices_to = None

    return limit_choices_to


def get_queryset(model_class, manager=None, limit_choices_to=None):
    if manager is not None and hasattr(model_class, manager):
        queryset = getattr(model_class, manager)
    else:
        queryset = model_class._default_manager

    if limit_choices_to:
        queryset = queryset.complex_filter(limit_choices_to)
    return queryset


def serialize_results(results):
    return [
        {'value': item.pk if str(item.pk).isdigit() else str(item.pk), 'display': force_text(item)} for item in results
    ]


def get_keywords(field, value, m2m=False):
    if value == '0':
        keywords = {str("%s__isnull" % field): True}
    elif m2m:
        keywords = {str("%s__pk" % field): str(value)}
    else:
        keywords = {str(field): str(value)}

    return keywords


def sort_results(results):
    """Performs in-place sort of filterchain results."""
    results.sort(key=lambda x: unicode_sorter(force_text(str(x))))
