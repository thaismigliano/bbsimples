from django.shortcuts import render
from django.http import HttpResponse
from . import forms
import urllib.request
import calendar
import math

from colour import Color
from bb_enxoval.models import Temperature


MONTHS = [calendar.month_abbr[i] for i in range(1, 13)]
BODY_CURTO_27 = [6, 8, 6, 6, 6]
BODY_CURTO_17 = [0, 2, 2, 2, 2]

BODY_LONGO_27 = [3, 2, 2, 2, 2]
BODY_LONGO_17 = [6, 6, 8, 8, 8]

CULOTE_27 = [4, 6, 6, 6, 6]
CULOTE_17 = [6, 6, 8, 8, 8]

MACACAO_CURTO_27 = [0, 6, 6, 6, 6]
MACACAO_CURTO_17 = [0, 0, 0, 0, 0]

MACACAO_LONGO_27 = [2, 2, 2, 2, 2]
MACACAO_LONGO_17 = [4, 6, 6, 6, 6]

CAMISETA_CURTA_27 = [0, 4, 4, 4, 4]
CAMISETA_CURTA_17 = [0, 2, 2, 2, 2]

CAMISETA_LONGA_27 = [0, 2, 2, 2, 2]
CAMISETA_LONGA_17 = [0, 4, 4, 4, 4]

CASAQUINHO_27 = [2, 1, 1, 1, 1]
CASAQUINHO_17 = [2, 3, 3, 3, 3]

MEIA = [3, 3, 6, 6, 6]

def get_color(x):
  x = max(min(round(x), 26), 17)
  # COLORS = ["#AED6F1", "#85C1E9",
  #           "#A3E4D7", "#76D7C4",
  #           "#F9E79F", "#F7DC6F",
  #           "#F5CBA7", "#EB984E",
  #           "#F1948A", "#EC7063"]
  COLORS = ["#AED6F1", "#AED6F1",
            "#A3E4D7", "#A3E4D7",
            "#F9E79F", "#F9E79F",
            "#F5CBA7", "#F5CBA7",
            "#F1948A", "#F1948A"]
  return COLORS[x - 17]

def get_city_temperature(city, month):
  temperatures = Temperature.objects.filter(city=city)
  t_avg = []
  t_min = []
  t_max = []
  for t in temperatures:
    color = get_color(t.t_avg_c)
    t_avg.append((t.t_avg_c, color))
    t_min.append((t.t_min_c, color))
    t_max.append((t.t_max_c, color))
  t_avg = [("T. média (°C)", "#D3D3D3")] + t_avg[month:] + t_avg[:month]
  t_min = [("T. mínima (°C)", "#D3D3D3")] + t_min[month:] + t_min[:month]
  t_max = [("T. máxima (°C)", "#D3D3D3")] + t_max[month:] + t_max[:month]
  data = [t_avg, t_min, t_max]
  return data



def calculate_num_clothes(q_27, q_17, temp):
  temp = [float(ele) for ele, _ in temp]
  temp = [temp[0],
          (temp[1] + temp[2]) / 2,
          (temp[3] + temp[4] + temp[5]) / 3,
          (temp[6] + temp[7] + temp[8]) / 3,
          (temp[9] + temp[10] + temp[11]) / 3]

  num_clothes = []
  cols = [1, 2, 3, 3, 3]
  for i in range(0, len(temp)):
    q = ((q_27[i] - q_17[i]) * (temp[i] - 17.0) / 10.0) + q_17[i]
    int_q = max(math.ceil(q), 0)
    num_clothes = num_clothes + [(int_q, cols[i])]
  return num_clothes


def form(request):
  form = forms.FormDateAndCity()

  if request.method == 'POST':
    form = forms.FormDateAndCity(request.POST)

    if form.is_valid():
      city = form.cleaned_data['city']
      url = form.cleaned_data['city'].climate_date_url
      month = int(form.cleaned_data['month']) - 1
      data = get_city_temperature(city, month)
      return render(request,
                    'bb_enxoval/bb_enxoval.html',
                    {'data': data,
                     'months': MONTHS[month:] + MONTHS[:month],
                     'body_curto': calculate_num_clothes(
                         BODY_CURTO_27,
                         BODY_CURTO_17,
                         data[0][1:]),
                     'body_longo': calculate_num_clothes(
                         BODY_LONGO_27,
                         BODY_LONGO_17,
                         data[0][1:]),
                     'culote': calculate_num_clothes(
                         CULOTE_27,
                         CULOTE_17,
                         data[0][1:]),
                     'macacao_curto': calculate_num_clothes(
                         MACACAO_CURTO_27,
                         MACACAO_CURTO_17,
                         data[0][1:]),
                     'macacao_longo': calculate_num_clothes(
                         MACACAO_LONGO_27,
                         MACACAO_LONGO_17,
                         data[0][1:]),
                     'camiseta_curta': calculate_num_clothes(
                         CAMISETA_CURTA_27,
                         CAMISETA_CURTA_17,
                         data[0][1:]),
                     'camiseta_longa': calculate_num_clothes(
                         CAMISETA_LONGA_27,
                         CAMISETA_LONGA_17,
                         data[0][1:]),
                     'casaquinho': calculate_num_clothes(
                         CASAQUINHO_27,
                         CASAQUINHO_17,
                         data[0][1:]),
                     'meia': calculate_num_clothes(
                         MEIA,
                         MEIA,
                         data[0][1:])})

  form.fields['city'].label = "Cidade: "
  form.fields['state'].label = "Estado: "
  form.fields['month'].label = "Mês do nascimento: "
  return render(request,
                'bb_enxoval/form_page.html',
                {'location_form': form})
