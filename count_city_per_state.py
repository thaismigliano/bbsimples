import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bbsimples.settings')

import django
django.setup()

from bb_enxoval.models import City, State
from smart_selects.utils import unicode_sorter

if __name__ == '__main__':
    states = State.objects.all()
    for state in states:
        cities = City.objects.filter(state=state)
        print(state.name + ": " + str(len(cities)))
