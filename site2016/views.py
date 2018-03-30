from django.shortcuts import render, HttpResponseRedirect
import sendgrid
from sendgrid.helpers.mail import *
from django.conf import settings
from .models import *

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
                          'professores': Professor.objects.all(),
                          'bolsistas': Aluno.objects.filter(situacao='B').order_by('nome', 'sobrenome'),
                          'nao_bolsistas': Aluno.objects.filter(situacao='N').order_by('nome', 'sobrenome'),
                          'voluntarios': Aluno.objects.filter(situacao='V').order_by('nome', 'sobrenome'),
                          'ex_membros': Aluno.objects.filter(situacao='E').order_by('nome', 'sobrenome'),
                          'DEBUG': settings.DEBUG}

    return render(request, 'site2016/equipe.html', context_dictionary)


def projetos(request):
    context_dictionary = {'pagina': 'projetos', 'DEBUG': settings.DEBUG}
    return render(request, 'site2016/projetos.html', context_dictionary)


def processo_seletivo(request, ano, semestre):
    print(ano)
    print(semestre)
    # TODO: modificar semestre
    ps = ProcessoSeletivo.objects.get(ano=ano, semestre=1)

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
               'data_inscricao_inicio': ps.data_inscricao_inicio.strftime("%d/%m"),
               'data_inscricao_fim': ps.data_inscricao_fim.strftime("%d/%m"),
               'etapas': etapas_dict,
               'requisitos': ps.requisitos,
               'email_inscricao': ps.email_inscricao,
               'edital': ps.edital.url
               }

    context_dictionary = {'pagina': 'processo_seletivo', 'DEBUG': settings.DEBUG, 'ps': ps_dict}
    return render(request, 'site2016/processoseletivo.html', context_dictionary)


def processo_seletivo_2017_1(request):
    context_dictionary = {'pagina': 'processo_seletivo_2016_2', 'DEBUG': settings.DEBUG}
    return render(request, 'site2016/processos_seletivos_anteriores/processoseletivo_2017_1.html', context_dictionary)


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
