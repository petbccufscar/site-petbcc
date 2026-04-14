from types import SimpleNamespace

from django.shortcuts import redirect, render

from django.core.mail import EmailMessage
from django.contrib import messages

from core.models import Atividade, Categoria, Membro, Projeto, ProcessoSeletivo

from core.forms import ContactForm

from datetime import date, timedelta
from django.utils import timezone
from django.db.models import Sum, F, IntegerField, ExpressionWrapper

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
    
    if categoria:
        PROJETOS = Projeto.objects.filter(categoria__slug=categoria)
    else:
        PROJETOS = Projeto.objects.all()

    PROJETOS = PROJETOS.filter(publico=True)

    return render(request, "core/projetos.html", {
        "projetos": PROJETOS,
        "categoria_ativa": categoria,
        "categorias": CATEGORIAS,
    })

def projeto(request, id):
    projeto = Projeto.objects.get(id=id)
    registros = Atividade.objects.filter(projeto=projeto).order_by("-data")

    # Não exibe os membros que já saíram do PET
    membros = projeto.membros.exclude(situacao=Membro.Situacao.EX_MEMBRO)

    return render(request, "core/projeto.html", {
        "PROJETO": projeto,
        "MEMBROS": membros,
        "REGISTROS": registros,
    })

def membro(request, id):
    membro = Membro.objects.get(id=id)

    projetos = Projeto.objects.filter(membros=membro, publico=True)
    registros = Atividade.objects.filter(membros=membro, projeto__publico=True).order_by("-data")

    def formatar_minutos(total):
        if not total:
            return "0h00min"
        
        horas = total // 60
        minutos = total % 60

        return f"{horas}h {minutos:02d}min"

    duracao_total = ExpressionWrapper(
        F("horas") * 60 + F("minutos"),
        output_field=IntegerField()
    )

    # ================== Soma semanal

    hoje = timezone.now().date()
    dias_desde_domingo = (hoje.weekday() + 1) % 7
    inicio_semana = hoje - timedelta(days=dias_desde_domingo)

    qs_semana = registros.filter(data__gte=inicio_semana)

    print("Inicio semana:", inicio_semana)
    print("Qtd registros semana:", qs_semana.count())

    soma_semanal = registros.filter(
        data__gte=inicio_semana
    ).aggregate(total=Sum(duracao_total))["total"]

    
    print(soma_semanal, "soma semanal")

    # ==================== Último mês

    primeiro_dia_mes_atual = hoje.replace(day=1)
    ultimo_dia_mes_passado = primeiro_dia_mes_atual - timedelta(days=1)
    primeiro_dia_mes_passado = ultimo_dia_mes_passado.replace(day=1)

    registros_mes = registros.filter(
        data__range=(primeiro_dia_mes_passado, ultimo_dia_mes_passado)
    )

    total_mes = registros_mes.aggregate(total=Sum(duracao_total))["total"]
    dias_mes = ultimo_dia_mes_passado.day

    media_ultimo_mes = (total_mes // dias_mes) if total_mes else 0

    # ============= Média último mês

    mes = primeiro_dia_mes_passado.month
    ano = primeiro_dia_mes_passado.year

    for _ in range(2):
        if mes == 1:
            mes = 12
            ano -= 1
        else:
            mes -= 1

    inicio_3_meses = date(ano, mes, 1)

    registros_3m = registros.filter(
        data__range=(inicio_3_meses, ultimo_dia_mes_passado)
    )

    total_3m = registros_3m.aggregate(total=Sum(duracao_total))["total"]
    dias_3m = (ultimo_dia_mes_passado - inicio_3_meses).days + 1

    media_ultimos_tres_meses = (total_3m // dias_3m) if total_3m else 0

    # ================== Soma total

    total_horas = registros.aggregate(total=Sum(duracao_total))["total"]

    sumario = {
        "soma_semanal": formatar_minutos(soma_semanal),
        "media_ultimo_mes": formatar_minutos(media_ultimo_mes),
        "media_ultimos_tres_meses": formatar_minutos(media_ultimos_tres_meses),
        "total_horas": formatar_minutos(total_horas)
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