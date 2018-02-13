from django import forms
from django.core import validators
from django.forms import extras
from django.forms.fields import ChoiceField
from bb_enxoval.models import Location
import calendar
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class FormDateAndCity(forms.ModelForm):
  MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1, 13)]

  month = ChoiceField(choices=MONTH_CHOICES)

  class Meta:
    model = Location
    fields = ('state', 'city',)
