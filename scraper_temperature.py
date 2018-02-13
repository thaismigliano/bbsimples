import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bbsimples.settings')

import django
django.setup()

import logging
import unittest
from bs4 import BeautifulSoup
from bb_enxoval.models import City, State, Temperature
from retry import retry
import urllib.request as urllib2


@retry(exceptions=Exception, tries=4, delay=3, backoff=2)
def urlopen_with_retry(city_link):
    return urllib2.urlopen(city_link)

def get_city_temperature(city):
  city_page = urlopen_with_retry(city.climate_date_url).read()
  city_soup = BeautifulSoup(city_page, "html.parser")
  data = []
  table = city_soup.find(id="weather_table")

  table_body = table.find('tbody')
  rows = table_body.find_all('tr')
  for row in rows[:7]:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])  # Get rid of empty values

  for month in range(0, 12):
      t_avg = data[0][month + 1]
      t_min = data[1][month + 1]
      t_max = data[2][month + 1]
      rain = data[6][month + 1]
      t = Temperature.objects.get_or_create(
          city=city,
          month=month,
          t_min_c=t_min,
          t_max_c=t_max,
          t_avg_c=t_avg,
          rain=rain)

if __name__ == '__main__':
    cities = City.objects.all()
    temperatures = Temperature.objects.all()

    d = {}
    for t in temperatures:
        d[t.city.id] = True

    i = 0
    num = len(cities)
    for city in cities:
        i = i + 1
        if city.id in d:
            continue
        print(str(i) + " / " + str(num))
        get_city_temperature(city)
