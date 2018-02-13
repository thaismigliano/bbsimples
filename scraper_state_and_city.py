import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bbsimples.settings')

import django
django.setup()

from bs4 import BeautifulSoup
from bb_enxoval.models import City, State
import urllib.request


BASIC_URL = "https://pt.climate-data.org"
BRAZIL_URL = BASIC_URL + "/country/114"


def get_cities_from_state(state_page, cities):
  state_soup = BeautifulSoup(state_page, "html.parser")
  for link in state_soup.find_all('a'):
    if "location" in link.get('href'):
      city_name = link.find("span", class_="name")
      if city_name:
        cities[city_name.get_text()] = BASIC_URL + link.get('href')


def get_last_page(state_page):
  state_soup = BeautifulSoup(state_page, "html.parser")

  last_page = 1
  for link in state_soup.find_all('a'):
    if "page" in link.get('href'):
      last_page = max(last_page, int(link.get('href')[8:]))
  return last_page

def get_or_create_state(state_name, state_link):
  state = State.objects.get_or_create(
      name=state_name, climate_date_url=state_link)[0]
  return state


def get_or_create_city(city_name, city_link, state):
  city = City.objects.get_or_create(
      name=city_name, state=state, climate_date_url=city_link)[0]
  return city


if __name__ == '__main__':
  brazil_page = urllib.request.urlopen(BRAZIL_URL).read()
  soup = BeautifulSoup(brazil_page, "html.parser")
  states = {}
  for link in soup.find_all('a'):
    if "region" not in link.get('href'):
      continue
    state_name = link.get_text()
    states[state_name] = BASIC_URL + link.get('href')

  for state_name, state_link in sorted(states.items()):
    print("State: " + state_name)
    state = get_or_create_state(state_name, state_link)
    cities = {}
    state_page = urllib.request.urlopen(state_link).read()
    # Get the cities from the first page.
    get_cities_from_state(state_page, cities)
    # Calculate the number of pages of this state.
    last_page = get_last_page(state_page)
    # Get the cities from this state in the other pages.
    for i in range(2, last_page):
      state_page = urllib.request.urlopen(
          state_link + "?page=" + str(i)).read()
      get_cities_from_state(state_page, cities)

    for city_name, city_link in cities.items():
      print("  City: " + city_name)
      city = get_or_create_city(city_name, city_link, state)

#
#   for city_name, city_link in cities.items():
#     print "City: " + city_name
#     get_city_temperature(city_link)
#   break
