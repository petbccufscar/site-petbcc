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

exMembros = [{'nome': 'Alan Cesar Laine', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Ana Dulce Padovan Torres', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'André Vinicius Bertoni Nicoleti', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Bruno Dias Leite', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Bruno F. Rodrigues', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Bruno Guerra D. Pereira', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Bruno Luigi Borgo', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Bruno Santos', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Caroline Castor dos Santos', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Denis Cappelini', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Douglas Antonio Martins Barbino', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Eduardo Kazuo Nakao', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Felipe Castro Dezotti', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Guilherme Cuppi Jeronimo', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Guilherme Rigo Reccio', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Hugo Leonardo M. A. de Barros', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Júlio Maçumoto', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Leonardo Lopes', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Lucas Antoniale Callegari', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Lucas Bueno', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Lucas Yamanaka', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Marcelo Araujo Pontes', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Mariana Yamamoto', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Matheus dos Santos Freitas', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Nicolas Masonori Shimizu', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Paula Lamin Honda', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Rafael Eduardo Wolf Goes', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Renan Peixoto da Silva', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Tiago Bassani', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Tiago Bonadio Badoco', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Thiago Arraiol Casaes', 'descricao': '', 'foto': 'user.png'},
             {'nome': 'Thiago Neves Romero', 'descricao': '', 'foto': 'user.png'}]


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
