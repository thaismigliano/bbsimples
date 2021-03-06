import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bbsimples.settings')

import django
django.setup()

from bb_enxoval.models import City, State
from smart_selects.utils import unicode_sorter

CIDADES = [
"Salvador",
"Feira de Santana",
"Vitória da Conquista",
"Camaçari",
"Itabuna",
"Juazeiro",
"Lauro de Freitas",
"Ilhéus",
"Jequié",
"Teixeira de Freitas",
"Barreiras",
"Alagoinhas",
"Porto Seguro",
"Simões Filho",
"Paulo Afonso",
"Eunápolis",
"Santo Antônio de Jesus",
"Valença",
"Candeias",
"Guanambi",
"Jacobina",
"Serrinha",
"Luís Eduardo Magalhães",
"Senhor do Bonfim",
"Dias d'Ávila",
"Itapetinga",
"Irecê",
"Campo Formoso",
"Casa Nova",
"Bom Jesus da Lapa",
"Brumado",
"Conceição do Coité",
"Itamaraju",
"Itaberaba",
"Cruz das Almas",
"Ipirá",
"Santo Amaro",
"Euclides da Cunha",
"Catu",
"Jaguaquara",
"Araci",
"Ribeira do Pombal",
"Barra",
"Santo Estêvão",
"Caetité",
"Tucano",
"Monte Santo",
"Macaúbas",
"Poções",
"Xique-Xique",
"Ipiaú",
"Livramento de Nossa Senhora",
"Mata de São João",
"Maragogipe",
"São Sebastião do Passé",
"Seabra",
"Nova Viçosa",
"Entre Rios",
"Vera Cruz",
"Remanso",
"Santa Maria da Vitória",
"Mucuri",
"Sento Sé",
"Jeremoabo",
"Rio Real",
"Inhambupe",
"São Francisco do Conde",
"Santaluz",
"Amargosa",
"Pojuca",
"São Gonçalo dos Campos",
"Itiúba",
"Esplanada",
"Morro do Chapéu",
"Camamu",
"Itapicuru",
"Riacho de Santana",
"Cansanção",
"Pilão Arcado",
"Curaçá",
"Cachoeira",
"Riachão do Jacuípe",
"Cícero Dantas",
"Barra do Choça",
"Jaguarari",
"Conceição do Jacuípe",
"Correntina",
"Camacan",
"São Desidério",
"Canavieiras",
"Gandu",
"Serra do Ramalho",
"Paratinga",
"Ruy Barbosa",
"Itabela",
"Capim Grosso",
"Muritiba",
"Carinhanha",
"Campo Alegre de Lourdes",
"Paripiranga",
"Irará",
"Nazaré",
"Ituberá",
"Prado",
"Santa Rita de Cássia",
"Quijingue",
"Valente",
"Santa Cruz Cabrália",
"Lapão",
"Itacaré",
"Iguaí",
"Presidente Tancredo Neves",
"Ibotirama",
"Miguel Calmon",
"Santana",
"Ubatã",
"Mundo Novo",
"Castro Alves",
"Olindina",
"Cândido Sales",
"Planalto",
"Canarana",
"Queimadas",
"Amélia Rodrigues",
"Conde",
"Iaçu",
"Nova Soure",
"Uauá",
"Formosa do Rio Preto",
"João Dourado",
"Iraquara",
"Piritiba",
"Ibirapitanga",
"Laje",
"Coração de Maria",
"Belmonte",
"Ibicaraí",
"Caculé",
"Sobradinho",
"Medeiros Neto",
"Rafael Jambeiro",
"Maracás",
"Alcobaça",
"Teofilândia",
"Riachão das Neves",
"Itambé",
"Mutuípe",
"Conceição da Feira",
"Oliveira dos Brejinhos",
"Itaparica",
"Caravelas",
"Palmas de Monte Alto",
"Boquira",
"Wenceslau Guimarães",
"Guaratinga",
"Barra da Estiva",
"Paramirim",
"São Felipe",
"Uruçuca",
"Una",
"Crisópolis",
"Itajuípe",
"Buritirama",
"Governador Mangabeira",
"Baixa Grande",
"Santa Bárbara",
"Tanhaçu",
"Taperoá",
"Maraú",
"Itororó",
"Pindobaçu",
"Ubaíra",
"Madre de Deus",
"Ubaitaba",
"Itanhém",
"Sátiro Dias",
"Itarantim",
]

if __name__ == '__main__':
    state = State.objects.filter(acronym="BA")
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
