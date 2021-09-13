from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import sendgrid
from sendgrid.helpers.mail import *
from django.conf import settings
from .models import *
from django.db.models import Sum
from datetime import date


def manutencao(request):
    return render(request, 'site2016/manutencao.html', {'DEBUG': settings.DEBUG})


def home(request):
    if not settings.MANUTENCAO:
        context_dictionary = {'pagina': 'home', 'DEBUG': settings.DEBUG}
        return render(request, 'site2016/home.html', context_dictionary)
    else:
        return render(request, 'site2016/manutencao.html', {})


def equipe(request):
    context_dictionary = {'pagina': 'equipe',
                          'professores': Professor.objects.listar_membros_ativos().order_by('nome', 'sobrenome'),
                          'bolsistas': Aluno.objects.listar_bolsistas().order_by('nome', 'sobrenome'),
                          'nao_bolsistas': Aluno.objects.listar_nao_bolsistas().order_by('nome', 'sobrenome'),
                          'colaboradores': Aluno.objects.listar_colaboradores().order_by('nome', 'sobrenome'),
                          'ex_membros': MembroEquipe.objects.listar_ex_membros().order_by('nome', 'sobrenome'),
                          'DEBUG': settings.DEBUG}

    return render(request, 'site2016/equipe.html', context_dictionary)


@login_required
def membro(request, id):
    membro = MembroEquipe.objects.get(id=id)
    projetos = membro.projetos.all()
    atividades = Atividade.objects.filter(membro__id=id).order_by('-dia')
    tempo = {
        'total': {'horas': 0, 'minutos': 0},
        'semana': {'horas': 0, 'minutos': 0},
        'mes': {'horas': 0, 'minutos': 0},
        '3meses': {'horas': 0, 'minutos': 0}
    }

    # as medias de horas sao calculadas num intervalo de dias,
    # ao inves de calcular um mes especifico
    # ou seja, a media pode mudar a cada dia que passa

    # calcula as datas de 7, 28 e 84 dias atras
    ultimaSemana = datetime.date.today() - datetime.timedelta(7)
    ultimoMes = datetime.date.today() - datetime.timedelta(28)
    ultimos3 = datetime.date.today() - datetime.timedelta(84)

    # a funcao annotate soma todo o tempo gasto para cada dia
    relatorio_atividades = (atividades.values('dia')
                            .annotate(horas=Sum('horas'))
                            .annotate(minutos=Sum('minutos'))
                            .order_by())

    dados_grafico = []

    for i, relatorio in enumerate(relatorio_atividades):

        if relatorio['dia'] >= ultimos3:

            # gera uma entrada apenas em minutos para projetar no grafico
            relatorio['tempo'] = (relatorio['horas'] * 60) + \
                (relatorio['minutos'])

            # incrementa o tempo total
            tempo['total']['horas'] += relatorio['horas']
            tempo['total']['minutos'] += relatorio['minutos']

            # incrementa cada intervalo se o dia da atividade estiver
            # entre hoje e a data limite
            if relatorio['dia'] >= ultimaSemana:
                tempo['semana']['horas'] += relatorio['horas']
                tempo['semana']['minutos'] += relatorio['minutos']

            if relatorio['dia'] >= ultimoMes:
                tempo['mes']['horas'] += relatorio['horas']
                tempo['mes']['minutos'] += relatorio['minutos']

            tempo['3meses']['horas'] += relatorio['horas']
            tempo['3meses']['minutos'] += relatorio['minutos']

            # adiciona o dia ao grafico
            dados_grafico.append(relatorio)

            # previne indexOutOfRange para as proximas operacoes
            if i < relatorio_atividades.count()-1:

                # calcula a distancia entre o dia da atividade atual e da proxima
                diff_atividades = relatorio_atividades[i +
                                                       1]['dia'] - relatorio_atividades[i]['dia']

                # caso a distancia seja maior que 1, adiciona dias vazios entre as atividades
                if diff_atividades > datetime.timedelta(days=1):

                    # loop para adicionar J dias a partir do dia atual
                    for J in range(1, diff_atividades.days):
                        dia_vazio = {
                            'dia': relatorio_atividades[i]['dia'] + datetime.timedelta(days=J),
                            'tempo': 0,
                        }

                        dados_grafico.append(dia_vazio)

    # adiciona dias vazios entre a ultima atividade e hoje
    diff_hoje = datetime.date.today() - dados_grafico[-1]['dia']

    if diff_hoje > datetime.timedelta(days=0):
        for J in range(1, diff_hoje.days+1):
            dia_vazio = {
                'dia': relatorio_atividades[i]['dia'] + datetime.timedelta(days=J),
                'tempo': 0,
            }

            dados_grafico.append(dia_vazio)

    # tira a media semanal do mes e dos ultimos 3 meses
    tempo['mes']['horas'] //= 4
    tempo['mes']['minutos'] //= 4
    tempo['3meses']['horas'] //= 12
    tempo['3meses']['minutos'] //= 12

    # formata os minutos de cada entrada
    if tempo['total']['minutos'] > 60:
        tempo['total']['horas'] += (tempo['total']['minutos'] // 60)
        tempo['total']['minutos'] = (tempo['total']['minutos'] % 60)

    if tempo['semana']['minutos'] > 60:
        tempo['semana']['horas'] += (tempo['semana']['minutos'] // 60)
        tempo['semana']['minutos'] = (tempo['semana']['minutos'] % 60)

    if tempo['mes']['minutos'] > 60:
        tempo['mes']['horas'] += (tempo['mes']['minutos'] // 60)
        tempo['mes']['minutos'] = (tempo['mes']['minutos'] % 60)

    if tempo['3meses']['minutos'] > 60:
        tempo['3meses']['horas'] += (tempo['3meses']['minutos'] // 60)
        tempo['3meses']['minutos'] = (tempo['3meses']['minutos'] % 60)

    # transforma o resultado em string para formatar com 0 padding
    tempo['semana']['horas'] = str(tempo['semana']['horas']).zfill(2)
    tempo['semana']['minutos'] = str(tempo['semana']['minutos']).zfill(2)
    tempo['mes']['horas'] = str(tempo['mes']['horas']).zfill(2)
    tempo['mes']['minutos'] = str(tempo['mes']['minutos']).zfill(2)
    tempo['3meses']['horas'] = str(tempo['3meses']['horas']).zfill(2)
    tempo['3meses']['minutos'] = str(tempo['3meses']['minutos']).zfill(2)
    tempo['total']['horas'] = str(tempo['total']['horas']).zfill(2)
    tempo['total']['minutos'] = str(tempo['total']['minutos']).zfill(2)

    context_dictionary = {
        'membro': membro,
        'projetos': projetos,
        'atividades': atividades,
        'dados_grafico': dados_grafico,
        'tempo': tempo,
        'DEBUG': settings.DEBUG
    }

    return render(request, 'site2016/membro.html', context_dictionary)


def projetos(request):

    projetos_desenvolvimento = []
    projetos_en_pesq_ex = []
    projetos_outros = []

    for projeto in Projeto.objects.order_by("nome"):

        projeto_obj = {
            'id': projeto.id,
            'nome': projeto.nome,
            'descricao': projeto.descricao,
            'publico': projeto.publico,
            'tecnologias': projeto.tecnologias.all(),
            'status': projeto.status,
            'imagem': projeto.imagem.url
        }

        for cat in projeto.categorias.all():
            if cat.sigla == 'DS':
                projetos_desenvolvimento.append(projeto_obj)
                break
            elif cat.sigla == 'O':
                projetos_outros.append(projeto_obj)
                break
            else:
                projetos_en_pesq_ex.append(projeto_obj)
                break

    tecnologias = []
    for tecnologia in Tecnologia.objects.order_by('nome'):
        tecnologias.append(
            {'nome': tecnologia.nome, 'imagem': tecnologia.imagem.url, 'link': tecnologia.link})

    context_dictionary = {'pagina': 'projetos', 'DEBUG': settings.DEBUG,
                          'projetos_desenvolvimento': projetos_desenvolvimento,
                          'tecnologias': tecnologias,
                          'projetos_en_pesq_ex': projetos_en_pesq_ex,
                          'projetos_outros': projetos_outros}

    return render(request, 'site2016/projetos.html', context_dictionary)


@login_required
def projeto(request, id):
    projeto = Projeto.objects.get(id=id)
    membros = projeto.membroequipe_set.all()
    atividades = Atividade.objects.filter(projeto__id=id).order_by('-dia')
    tempo = {
        'total': {'horas': 0, 'minutos': 0},
        'semana': {'horas': 0, 'minutos': 0},
        'mes': {'horas': 0, 'minutos': 0},
        '3meses': {'horas': 0, 'minutos': 0}
    }

    relatorio_atividades = (atividades.values('dia')
                            .annotate(horas=Sum('horas'))
                            .annotate(minutos=Sum('minutos'))
                            .order_by())

    # logica comentada na rota membro
    ultimaSemana = datetime.date.today() - datetime.timedelta(7)
    ultimoMes = datetime.date.today() - datetime.timedelta(28)
    ultimos3 = datetime.date.today() - datetime.timedelta(84)

    dados_grafico = []

    for i, relatorio in enumerate(relatorio_atividades):

        if relatorio['dia'] >= ultimos3:

            relatorio['tempo'] = (relatorio['horas'] * 60) + \
                (relatorio['minutos'])

            tempo['total']['horas'] += relatorio['horas']
            tempo['total']['minutos'] += relatorio['minutos']

            if relatorio['dia'] >= ultimaSemana:
                tempo['semana']['horas'] += relatorio['horas']
                tempo['semana']['minutos'] += relatorio['minutos']

            if relatorio['dia'] >= ultimoMes:
                tempo['mes']['horas'] += relatorio['horas']
                tempo['mes']['minutos'] += relatorio['minutos']

            tempo['3meses']['horas'] += relatorio['horas']
            tempo['3meses']['minutos'] += relatorio['minutos']

            dados_grafico.append(relatorio)

            if i < relatorio_atividades.count()-1:
                diff_atividades = relatorio_atividades[i +
                                                       1]['dia'] - relatorio_atividades[i]['dia']

                if diff_atividades > datetime.timedelta(days=1):
                    for J in range(1, diff_atividades.days):
                        dia_vazio = {
                            'dia': relatorio_atividades[i]['dia'] + datetime.timedelta(days=J),
                            'tempo': 0,
                        }

                        dados_grafico.append(dia_vazio)

    diff_hoje = datetime.date.today() - dados_grafico[-1]['dia']

    if diff_hoje > datetime.timedelta(days=0):
        for J in range(1, diff_hoje.days+1):
            dia_vazio = {
                'dia': relatorio_atividades[i]['dia'] + datetime.timedelta(days=J),
                'tempo': 0,
            }

            dados_grafico.append(dia_vazio)

    tempo['mes']['horas'] //= 4
    tempo['mes']['minutos'] //= 4
    tempo['3meses']['horas'] //= 12
    tempo['3meses']['minutos'] //= 12

    if tempo['total']['minutos'] > 60:
        tempo['total']['horas'] += (tempo['total']['minutos'] // 60)
        tempo['total']['minutos'] = (tempo['total']['minutos'] % 60)

    if tempo['semana']['minutos'] > 60:
        tempo['semana']['horas'] += (tempo['semana']['minutos'] // 60)
        tempo['semana']['minutos'] = (tempo['semana']['minutos'] % 60)

    if tempo['mes']['minutos'] > 60:
        tempo['mes']['horas'] += (tempo['mes']['minutos'] // 60)
        tempo['mes']['minutos'] = (tempo['mes']['minutos'] % 60)

    if tempo['3meses']['minutos'] > 60:
        tempo['3meses']['horas'] += (tempo['3meses']['minutos'] // 60)
        tempo['3meses']['minutos'] = (tempo['3meses']['minutos'] % 60)

    tempo['semana']['horas'] = str(tempo['semana']['horas']).zfill(2)
    tempo['semana']['minutos'] = str(tempo['semana']['minutos']).zfill(2)
    tempo['mes']['horas'] = str(tempo['mes']['horas']).zfill(2)
    tempo['mes']['minutos'] = str(tempo['mes']['minutos']).zfill(2)
    tempo['3meses']['horas'] = str(tempo['3meses']['horas']).zfill(2)
    tempo['3meses']['minutos'] = str(tempo['3meses']['minutos']).zfill(2)
    tempo['total']['horas'] = str(tempo['total']['horas']).zfill(2)
    tempo['total']['minutos'] = str(tempo['total']['minutos']).zfill(2)

    context_dictionary = {
        'projeto': projeto,
        'membros': membros,
        'atividades': atividades,
        'dados_grafico': dados_grafico,
        'tempo': tempo,
        'DEBUG': settings.DEBUG
    }

    return render(request, 'site2016/projeto.html', context_dictionary)


def processo_seletivo(request, ano, semestre):
    ps = ProcessoSeletivo.objects.get(ano=ano, semestre=semestre)

    etapas_dict = []

    for etapa in ps.etapas.order_by('ordem', 'data_inicio'):
        etapas_dict.append({
            'titulo': etapa.titulo,
            'data_inicio': etapa.data_inicio.strftime("%d/%m"),
            'data_fim': etapa.data_fim.strftime("%d/%m") if etapa.data_fim else None,
            'mostrar_hora': etapa.mostrar_hora,
            'horario': etapa.data_inicio.strftime("%H:%M"),
            'data_resultado': etapa.data_resultado.strftime("%d/%m") if etapa.data_resultado else None,
            'mostrar_resultado': etapa.mostrar_resultado,
            'resultado': etapa.resultado
        })

    ps_dict = {'edicao': str(ps.ano) + "/" + str(ps.semestre),
               'resultado_divulgado': not ps.ativo,
               'vagas_bolsista': ps.vagas_bolsista,
               'vagas_nao_bolsista': ps.vagas_nao_bolsista,
               'vagas_colaborador': ps.vagas_colaborador,
               'data_inscricao_inicio': ps.data_inscricao_inicio.strftime("%d/%m"),
               'data_inscricao_fim': ps.data_inscricao_fim.strftime("%d/%m"),
               'etapas': etapas_dict,
               'requisitos': ps.requisitos,
               'email_inscricao': ps.email_inscricao,
               'edital': ps.edital.url
               }

    context_dictionary = {'pagina': 'processo_seletivo',
                          'DEBUG': settings.DEBUG, 'ps': ps_dict}
    return render(request, 'site2016/processoseletivo.html', context_dictionary)


def contato(request):
    if request.method == 'POST':
        try:
            nome = request.POST['nome']
            email = request.POST['email']
            assunto = request.POST['assunto']
            mensagem = request.POST['mensagem']

            sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
            from_email = Email(nome+" <"+email+">")
            subject = "CONTATO VIA SITE: "+assunto
            to_email = Email("PET-BCC <petbcc@googlegroups.com>")

            conteudo_email = mensagem

            content = Content("text/html", conteudo_email)
            ready_mail = Mail(from_email, subject, to_email, content)

            response = sg.client.mail.send.post(request_body=ready_mail.get())
            print(response.status_code)
            print(response.body)
            print(response.headers)
            # TODO: implementar mensagem de feedback ao usuário
        except:
            pass

        context_dictionary = {'pagina': 'contato', 'DEBUG': settings.DEBUG}
        return render(request, 'site2016/contato.html', context_dictionary)
    else:
        context_dictionary = {'pagina': 'contato', 'DEBUG': settings.DEBUG}
        return render(request, 'site2016/contato.html', context_dictionary)


""" Manual C """


def manual_c(request):
    context_dictionary = {'pagina': 'manual_c', 'DEBUG': settings.DEBUG}
    return render(request, 'site2016/manualC/home.html', context_dictionary)


def sobre(request):
    context_dictionary = {'pagina': 'sobre', 'DEBUG': settings.DEBUG}
    return render(request, 'site2016/manualC/sobre.html', context_dictionary)


def math_h(request):
    context_dictionary = {'pagina': 'math_h', 'DEBUG': settings.DEBUG}
    return render(request, 'site2016/manualC/math/math_h.html', context_dictionary)


def math_funcoes(request):
    context_dictionary = {'pagina': 'math_funcoes', 'DEBUG': settings.DEBUG}
    return render(request, 'site2016/manualC/math/math_funcoes.html', context_dictionary)


def assert_h(request):
    context_dictionary = {'pagina': 'assert_h', 'DEBUG': settings.DEBUG}
    return render(request, 'site2016/manualC/assert/assert_h.html', context_dictionary)


def assert_funcoes(request):
    context_dictionary = {'pagina': 'assert_funcoes', 'DEBUG': settings.DEBUG}
    return render(request, 'site2016/manualC/assert/assert_funcoes.html', context_dictionary)


def ctype_h(request):
    context_dictionary = {'pagina': 'ctype_h', 'DEBUG': settings.DEBUG}
    return render(request, 'site2016/manualC/ctype/ctype_h.html', context_dictionary)


def ctype_funcoes(request):
    context_dictionary = {'pagina': 'ctype_funcoes', 'DEBUG': settings.DEBUG}
    return render(request, 'site2016/manualC/ctype/ctype_funcoes.html', context_dictionary)

def string_h(request):
    context_dictionary = {'pagina': 'string_h', 'DEBUG': settings.DEBUG}
    return render(request, 'site2016/manualC/string/string_h.html', context_dictionary)

def string_funcoes(request):
    context_dictionary = {'pagina': 'string_funcoes', 'DEBUG': settings.DEBUG}
    return render(request, 'site2016/manualC/string/string_funcoes.html', context_dictionary)
  
def errno_h(request):
    context_dictionary = {'pagina': 'errno_h', 'DEBUG': settings.DEBUG}
    return render(request, 'site2016/manualC/errno/errno_h.html', context_dictionary)


