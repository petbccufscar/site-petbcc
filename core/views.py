from types import SimpleNamespace

from django.shortcuts import redirect, render

from django.core.mail import EmailMessage
from django.contrib import messages

from core.models import Atividade, Categoria, Membro, Projeto, ProcessoSeletivo

from core.forms import ContactForm

from datetime import date

def inicio(request):
    return render(request, 'core/inicio.html')

def equipe(request):
    MEMBROS = Membro.objects.all()

    BOLSISTAS = MEMBROS.filter(situacao=Membro.Situacao.BOLSISTA)
    NAO_BOLSISTAS = MEMBROS.filter(situacao=Membro.Situacao.NAO_BOLSISTA)
    COLABORADORES = MEMBROS.filter(situacao=Membro.Situacao.COLABORADOR)
    EX_MEMBROS = MEMBROS.filter(situacao=Membro.Situacao.EX_MEMBRO)

    return render(request, 'core/equipe.html', {
        "BOLSISTAS": BOLSISTAS,
        "NAO_BOLSISTAS": NAO_BOLSISTAS,
        "COLABORADORES": COLABORADORES,
        "EX_MEMBROS": EX_MEMBROS
    })

def projetos(request):
    categoria = request.GET.get("categoria")

    CATEGORIAS = Categoria.objects.all().filter(interna=False)
    
    # TODO: Substituir por filtro em consulta ao banco de dados
    if categoria:
        PROJETOS = Projeto.objects.filter(categoria__slug=categoria)
    else:
        PROJETOS = Projeto.objects.all()

    return render(request, "core/projetos.html", {
        "projetos": PROJETOS,
        "categoria_ativa": categoria,
        "categorias": CATEGORIAS,
    })

def projeto(request, id):
    projeto = Projeto.objects.get(id=id)
    registros = Atividade.objects.filter(projeto=projeto).order_by("-data")

    return render(request, "core/projeto.html", {
        "projeto": projeto,
        "registros": registros,
    })

def membro(request, id):
    membro = Membro.objects.get(id=id)
    projetos = Projeto.objects.filter(membros=membro)
    registros = Atividade.objects.filter(membros=membro)

    # TODO: Calcular o total de horas
    sumario = {
        "soma_semanal": "8h35min",
        "media_ultimo_mes": "6h10min",
        "media_ultimos_tres_meses": "7h20min",
        "total_horas": "180h55min"
    }

    return render(request, "core/membro.html", {
        "membro": membro,
        "projetos": projetos,
        "registros": registros,
        "sumario": sumario
    })

def processo_seletivo(request):
    PS_ATUAL = ProcessoSeletivo.objects.order_by('-ano', '-semestre').first()
    ETAPAS = PS_ATUAL.etapas.all() if PS_ATUAL else []

    return render(request, "core/processo_seletivo.html", {
        "VAGAS": {
            "BOLSISTA": PS_ATUAL.vagas_bolsista if PS_ATUAL else 0,
            "NAO_BOLSISTA": PS_ATUAL.vagas_nao_bolsista if PS_ATUAL else 0,
            "COLABORADOR": PS_ATUAL.vagas_colaborador if PS_ATUAL else 0
        },
        "ETAPAS": ETAPAS,
        "PROCESSO": PS_ATUAL,
        "JA_FECHOU": PS_ATUAL.fim_inscricao < date.today() if PS_ATUAL else False
    })

def contato(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            result = EmailMessage(
                subject=f"CONTATO VIA SITE: {form.cleaned_data['subject']}",
                body=form.cleaned_data["message"],
                from_email=f"{form.cleaned_data['name']} <{form.cleaned_data['email']}>",
                to=["petbcc.ufscar@gmail.com"],
                reply_to=[form.cleaned_data["email"]],
            ).send()

            print("Email enviado com sucesso!" if result else "Falha ao enviar email.")

            messages.success(request, "Mensagem enviada com sucesso!")

            return redirect("core:contato") 
    else:
        form = ContactForm()

    return render(request, "core/contato.html", {"form": form})