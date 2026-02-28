from django.shortcuts import render
from datetime import date

def inicio(request):
    return render(request, 'core/inicio.html')

def equipe(request):
    return render(request, 'core/equipe.html', {
        "bolsistas": [
            {
                "nome": "Alice Silva",
                "descricao": "Tutor",
            },
            {
                "nome": "Bruno Costa",
                "descricao": "BCC 24",
            },
            {
                "nome": "Carla Souza",
                "descricao": "BCC 23",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            }
        ],
        "nao_bolsistas": [
            {
                "nome": "Alice Silva",
                "descricao": "Tutor",
            },
            {
                "nome": "Bruno Costa",
                "descricao": "BCC 24",
            },
            {
                "nome": "Carla Souza",
                "descricao": "BCC 23",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
        ],
        "colaboradores": [
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            }
        ],
        "ex_membros": [
            {
                "nome": "Alice Silva",
                "descricao": "Tutor",
            },
            {
                "nome": "Bruno Costa",
                "descricao": "BCC 24",
            },
            {
                "nome": "Carla Souza",
                "descricao": "BCC 23",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            },
            {
                "nome": "Diego Lima",
                "descricao": "BCC 22",
            }
        ]
    })

def projetos(request):
    categoria = request.GET.get("categoria")

    # TODO: Substituir por consulta ao banco de dados
    projetos_mock = [
        {
            "id": 1,
            "nome": "Sistema PET",
            "publico": True,
            "inicio": date(2024, 1, 10),
            "fim": None,
            "status": "ativo",
            "descricao": "Sistema interno para gerenciamento do PET.",
            "categoria": {
                "id": 1,
                "nome": "Desenvolvimento",
                "slug": "desenvolvimento"
            },
            "tecnologias": ["Django", "React", "PostgreSQL"],
            "imagem": "img/projeto1.jpg",
            "github": "https://github.com/"
        },
        {
            "id": 2,
            "nome": "Oficina de Programacao",
            "publico": True,
            "inicio": date(2023, 3, 15),
            "fim": date(2023, 12, 10),
            "status": "finalizado",
            "descricao": "Projeto de ensino voltado para iniciantes.",
            "categoria": {
                "id": 2,
                "nome": "Ensino",
                "slug": "ensino"
            },
            "tecnologias": ["Python", "Scratch"],
            "imagem": "img/projeto2.jpg",
            "github": "https://github.com/"
        },
        {
            "id": 3,
            "nome": "Pesquisa IA",
            "publico": False,
            "inicio": date(2025, 2, 1),
            "fim": None,
            "status": "planejamento",
            "descricao": "Estudo sobre aplicacoes de IA na educacao.",
            "categoria": {
                "id": 3,
                "nome": "Pesquisa",
                "slug": "pesquisa"
            },
            "tecnologias": ["Python", "TensorFlow"],
            "imagem": "img/projeto3.jpg",
            "github": "https://github.com/"
        },
        {
            "id": 4,
            "nome": "Extensão de Programação",
            "publico": True,
            "inicio": date(2024, 10, 1),
            "fim": None,
            "status": "suspenso",
            "descricao": "Projeto de extensao voltado a comunidade.",
            "categoria": {
                "id": 4,
                "nome": "Extensão",
                "slug": "extensao"
            },
            "tecnologias": ["Python", "TensorFlow"],
            "imagem": "img/projeto3.jpg",
            "github": "https://github.com/"
        },
    ]

    # TODO: Substituir por filtro em consulta ao banco de dados
    if categoria:
        projetos_mock = [projeto for projeto in projetos_mock if projeto["categoria"]["slug"] == categoria]

    categorias = [{
        "nome": "Ensino",
        "slug": "ensino"
    }, {
        "nome": "Pesquisa",
        "slug": "pesquisa"
    }, {
        "nome": "Extensão",
        "slug": "extensao"
    }, {
        "nome": "Desenvolvimento",
        "slug": "desenvolvimento"
    }]

    return render(request, "core/projetos.html", {
        "projetos": projetos_mock,
        "categoria_ativa": categoria,
        "categorias": categorias,
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
    return render(request, 'core/contato.html')

def manual_c(request):
    return render(request, 'core/manual_c.html')