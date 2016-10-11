from django.shortcuts import render

# Create your views here.

bolsistas = [{'nome': 'Alexandre da Silva Lara Pinto', 'ano': '014', 'foto': 'alexandre_da_silva_lara_pinto.jpg'},
             {'nome': 'Felipe Sampaio de Souza', 'ano': '015', 'foto': 'felipe_sampaio_de_souza.jpg'},
             {'nome': 'Gabriel Toret Palomino', 'ano': '013', 'foto': 'gabriel_toret_palomino.jpg'},
             {'nome': 'José Vitor de Carvalho Aquino', 'ano': '014', 'foto': 'jose_vitor_de_carvalho_aquino.jpg'},
             {'nome': 'Leonardo Destro Bronzato', 'ano': '013', 'foto': 'leonardo_desto_bronzato.jpg'},
             {'nome': 'Leticia Yumi Katsurada', 'ano': '015', 'foto': 'leticia_yumi_katsurada.jpg'},
             {'nome': 'Marcelo de Oliveira da Silva', 'ano': '012', 'foto': 'marcelo_de_oliveira_da_silva.jpg'},
             {'nome': 'Muriel Guilherme Alves Mauch', 'ano': '014', 'foto': 'muriel_guilherme_alves_mauch.jpg'},
             {'nome': 'Pedro Henrique Migliati', 'ano': '015', 'foto': 'pedro_henrique_miglitatti.jpg'},
             {'nome': 'Thiago Yonamine', 'ano': '014', 'foto': 'thiago_yonamine.jpg'}]


def home(request):
    context_dictionary = {'pagina': 'home'}
    return render(request, 'site2016/home.html', context_dictionary)


def equipe(request):
    context_dictionary = {'pagina': 'equipe', 'integrantes': bolsistas}
    return render(request, 'site2016/equipe.html', context_dictionary)


def projetos(request):
    context_dictionary = {'pagina': 'projetos'}
    return render(request, 'site2016/projetos.html', context_dictionary)


def exemplo_foundation(request):
    return render(request, 'site2016/ExemplosFoundation/index.html', {})
