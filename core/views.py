from django.shortcuts import redirect, render

from django.core.mail import EmailMessage
from django.contrib import messages

from core.models import Categoria, Membro, Projeto

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

    CATEGORIAS = Categoria.objects.all()
    
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

def processo_seletivo(request):
    vagas = [
        {
            "categoria": "Bolsista",
            "descricao": """O PET pode ter até <strong>12 alunos bolsistas</strong>, que recebem uma bolsa de <strong>R$700,00</strong> mensalmente.

A dedicação é de <strong>20 horas semanais</strong> e a participação no PET garante ao aluno participação em 60 horas de atividades complementares elegíveis no curso de Ciência da Computação.
""",
            "qtd_vagas": 12,
        },
        {
            "categoria": "Não-Bolsista",
            "descricao": """Caso todas as vagas para alunos bolsistas já estejam preenchidas, o PET pode ainda ter <strong>6 alunos</strong> atuando como não-bolsistas.

As condições são as mesmas dos bolsistas, bem como o certificado, que também vale como Atividades Complementares.
""",
            "qtd_vagas": 6,
        },
        {
            "categoria": "Colaborador",
            "descricao": """Caso as vagas para bolsistas e não-bolsistas já estiverem preenchidas, ainda é possível ser um membro do PET como colaborador.

Mesmo como colaborador você terá participação efetiva nos projetos, garantindo muito conhecimento e um grande incremento em sua graduação.
""",
            "qtd_vagas": "-",
        },
    ]

    etapas = [
        {
            "etapa": 1,
            "titulo": "Apresentação individual via vídeo",
            "descricao": "Envio de vídeo de apresentação pessoal com tema livre",
            "data_inicio": "26/08",
            "data_fim": "07/09",
            "data_resultado": "16/09",
        },
        {
            "etapa": 2,
            "titulo": "Proposta de projeto para o PET BCC",
            "descricao": "Elaboração de um documento contendo uma proposta de projeto real",
            "data_inicio": "23/09",
            "data_fim": "05/10",
            "data_resultado": None,
        },
        {
            "etapa": 3,
            "titulo": "Entrevista individual e arguição da Etapa 2",
            "descricao": "Entrevista online sobre a Etapa 2 junto com entrevista pessoal",
            "data_inicio": "06/10",
            "data_fim": "10/10",
            "data_resultado": "21/10",
        },
    ]

    return render(request, "core/processo_seletivo.html", {
        "vagas": vagas,
        "etapas": etapas,
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

def manual_c(request):
    return render(request, 'core/manual_c.html')