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


def processo_seletivo(request):
    context_dictionary = {'pagina': 'processo_seletivo', 'DEBUG': settings.DEBUG}
    return render(request, 'site2016/processoseletivo.html', context_dictionary)


def processo_seletivo_2016_2(request):
    context_dictionary = {'pagina': 'processo_seletivo', 'DEBUG': settings.DEBUG}
    return render(request, 'site2016/processos_seletivos_anteriores/processoseletivo_2016_2.html', context_dictionary)


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

            # TODO: implementar mensagem de feedback ao usuário
        except:
            pass

        context_dictionary = {'pagina': 'contato', 'DEBUG': settings.DEBUG}
        return render(request, 'site2016/contato.html', context_dictionary)
    else:
        context_dictionary = {'pagina': 'contato', 'DEBUG': settings.DEBUG}
        return render(request, 'site2016/contato.html', context_dictionary)
