from django.shortcuts import render

# Create your views here.

professores = [{'nome': 'Dr. Valter Vieira de Camargo', 'descricao': 'Tutor do PET-BCC e Coordenador do Curso',
                'foto': 'valter_vieira_de_camargo.jpg', 'contato': ''},
               {'nome': 'Dr. Antonio Carlos dos Santos', 'descricao': 'Professor colaborador',
                'foto': 'antonio_carlos_dos_santos.png', 'contato': ''},
               {'nome': 'Dr.ª Rosângela Ap. Dellosso Penteado', 'descricao': 'Professora colaboradora',
                'foto': 'gabriel_toret_palomino.jpg', 'contato': ''}]

bolsistas = [
    {'nome': 'Alexandre da Silva Lara Pinto', 'descricao': 'BCC 014', 'foto': 'alexandre_da_silva_lara_pinto.jpg'},
    {'nome': 'Felipe Sampaio de Souza', 'descricao': 'BCC 015', 'foto': 'felipe_sampaio_de_souza.jpg'},
    {'nome': 'Gabriel Toret Palomino', 'descricao': 'BCC 013', 'foto': 'gabriel_toret_palomino.jpg'},
    {'nome': 'José Vitor de Carvalho Aquino', 'descricao': 'BCC 014', 'foto': 'jose_vitor_de_carvalho_aquino.jpg'},
    {'nome': 'Leonardo Destro Bronzato', 'descricao': 'BCC 013', 'foto': 'leonardo_desto_bronzato.jpg'},
    {'nome': 'Leticia Yumi Katsurada', 'descricao': 'BCC 015', 'foto': 'leticia_yumi_katsurada.jpg'},
    {'nome': 'Marcelo de Oliveira da Silva', 'descricao': 'BCC 012', 'foto': 'marcelo_de_oliveira_da_silva.jpg'},
    {'nome': 'Muriel Guilherme Alves Mauch', 'descricao': 'BCC 014', 'foto': 'muriel_guilherme_alves_mauch.jpg'},
    {'nome': 'Pedro Henrique Migliati', 'descricao': 'BCC 015', 'foto': 'pedro_henrique_miglitatti.jpg'},
    {'nome': 'Thiago Yonamine', 'descricao': 'BCC 014', 'foto': 'thiago_yonamine.jpg'}]

naoBolsistas = [
    {'nome': 'Alexandre da Silva Lara Pinto', 'descricao': 'BCC 014', 'foto': 'alexandre_da_silva_lara_pinto.jpg'},
    {'nome': 'Felipe Sampaio de Souza', 'descricao': 'BCC 015', 'foto': 'felipe_sampaio_de_souza.jpg'},
    {'nome': 'Gabriel Toret Palomino', 'descricao': 'BCC 013', 'foto': 'gabriel_toret_palomino.jpg'}]

voluntarios = [{'nome': 'Fernando Messias da Silva', 'descricao': 'BCC 012', 'foto': 'fernando_messias_da_silva.jpg'},
               {'nome': 'Julia de Moura Caetano', 'descricao': 'BCC 015', 'foto': 'julia_de_moura_caetano.jpg'},
               {'nome': 'Miguel de Souza Tosta', 'descricao': 'BCC 015', 'foto': 'miguel_de_souza_tosta.jpg'}]

exMembros = [{'nome': 'Alan Cesar Laine', 'descricao': ''},
             {'nome': 'Ana Dulce Padovan Torres', 'descricao': ''},
             {'nome': 'André Vinicius Bertoni Nicoleti', 'descricao': ''},
             {'nome': 'Bruno Dias Leite', 'descricao': ''},
             {'nome': 'Bruno F. Rodrigues', 'descricao': ''},
             {'nome': 'Bruno Guerra D. Pereira', 'descricao': ''},
             {'nome': 'Bruno Luigi Borgo', 'descricao': ''},
             {'nome': 'Bruno Santos', 'descricao': ''},
             {'nome': 'Caroline Castor dos Santos', 'descricao': ''},
             {'nome': 'Denis Cappelini', 'descricao': ''},
             {'nome': 'Douglas Antonio Martins Barbino', 'descricao': ''},
             {'nome': 'Eduardo Kazuo Nakao', 'descricao': ''},
             {'nome': 'Felipe Castro Dezotti', 'descricao': ''},
             {'nome': 'Guilherme Cuppi Jeronimo', 'descricao': ''},
             {'nome': 'Guilherme Rigo Reccio', 'descricao': ''},
             {'nome': 'Hugo Leonardo M. A. de Barros', 'descricao': ''},
             {'nome': 'Júlio Maçumoto', 'descricao': ''},
             {'nome': 'Leonardo Lopes', 'descricao': ''},
             {'nome': 'Lucas Antoniale Callegari', 'descricao': ''},
             {'nome': 'Lucas Bueno', 'descricao': ''},
             {'nome': 'Lucas Yamanaka', 'descricao': ''},
             {'nome': 'Marcelo Araujo Pontes', 'descricao': ''},
             {'nome': 'Mariana Yamamoto', 'descricao': ''},
             {'nome': 'Matheus dos Santos Freitas', 'descricao': ''},
             {'nome': 'Nicolas Masonori Shimizu', 'descricao': ''},
             {'nome': 'Paula Lamin Honda', 'descricao': ''},
             {'nome': 'Rafael Eduardo Wolf Goes', 'descricao': ''},
             {'nome': 'Renan Peixoto da Silva', 'descricao': ''},
             {'nome': 'Tiago Bassani', 'descricao': ''},
             {'nome': 'Tiago Bonadio Badoco', 'descricao': ''},
             {'nome': 'Thiago Arraiol Casaes', 'descricao': ''},
             {'nome': 'Thiago Neves Romero', 'descricao': ''}]


def home(request):
    context_dictionary = {'pagina': 'home'}
    return render(request, 'site2016/home.html', context_dictionary)


def equipe(request):
    context_dictionary = {'pagina': 'equipe',
                          'professores': professores,
                          'bolsistas': bolsistas,
                          'naoBolsistas': naoBolsistas,
                          'voluntarios': voluntarios,
                          'exMembros': exMembros}
    return render(request, 'site2016/equipe.html', context_dictionary)


def projetos(request):
    context_dictionary = {'pagina': 'projetos'}
    return render(request, 'site2016/projetos.html', context_dictionary)


def sobre(request):
    context_dictionary = {'pagina': 'sobre'}
    return render(request, 'site2016/sobre.html', context_dictionary)
