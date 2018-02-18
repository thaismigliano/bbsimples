import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bbsimples.settings')

import django
django.setup()

from bb_enxoval.models import City, State
from smart_selects.utils import unicode_sorter

CIDADES = [
"Curitiba",
"Londrina",
"Maringá",
"Ponta Grossa",
"Cascavel",
"São José dos Pinhais",
"Foz do Iguaçu",
"Colombo",
"Guarapuava",
"Paranaguá",
"Araucária",
"Toledo",
"Apucarana",
"Pinhais",
"Campo Largo",
"Arapongas",
"Almirante Tamandaré",
"Umuarama",
"Piraquara",
"Cambé",
"Fazenda Rio Grande",
"Campo Mourão",
"Sarandi",
"Francisco Beltrão",
"Paranavaí",
"Pato Branco",
"Cianorte",
"Telêmaco Borba",
"Castro",
"Rolândia",
"Irati",
"União da Vitória",
"Ibiporã",
"Prudentópolis",
"Marechal Candido Rondon",
"Cornélio Procópio",
"Palmas",
"Lapa",
"Santo Antônio da Platina",
"Medianeira",
"São Mateus do Sul",
"Campina Grande do Sul",
"Jacarezinho",
"Paiçandu",
"Dois Vizinhos",
"Guaratuba",
"Marialva",
"Jaguariaíva",
"Mandaguari",
"Assis Chateaubriand",
"Palmeira",
"Rio Negro",
"Quedas do Iguaçu",
"Matinhos",
"Guaira",
"Ivaiporã",
"Bandeirantes",
"Rio Branco do Sul",
"Laranjeiras do Sul",
"Pitanga",
"Pinhão",
"Imbituva",
"Palotina",
"Ibaiti",
"Goioerê",
"Nova Esperança",
"Campo Magro",
"Arapoti",
"São Miguel do Iguaçu",
"Itaperuçu",
"Reserva",
"Astorga",
"Santa Helena",
"Cambará",
"Mandirituba",
"Piraí do Sul",
"Pontal do Paraná",
"Colorado",
"Ortigueira",
"Santa Terezinha de Itaipu",
"Loanda",
"Quatro Barras",
"Carambeí",
"Mandaguaçu",
"Altônia",
"Ubiratã",
"Coronel Vivida",
"Jandaia do Sul",
"Cruzeiro do Oeste",
"Andirá",
"Tibagi",
"Siqueira Campos",
"Santo Antônio do Sudoeste",
]

if __name__ == '__main__':
    state = State.objects.filter(acronym="PR")
    cities = City.objects.filter(state=state)
    # city_names = {}
    # for city in cities:
    #     city_names[city.name] = True
    # for city in CIDADES:
    #     if city not in city_names:
    #         print(city)
    for city in cities:
        if city.name not in CIDADES:
            city.delete()
