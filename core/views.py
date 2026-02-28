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
    return render(request, 'core/processo_seletivo.html')

def contato(request):
    return render(request, 'core/contato.html')

def manual_c(request):
    return render(request, 'core/manual_c.html')