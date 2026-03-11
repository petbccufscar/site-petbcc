from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Usuario(AbstractBaseUser):
    # O campo 'password'já existe dentro do AbstractBaseUser
    usuario = models.CharField(max_length=150, unique=True)
    # O Django obriga a definir qual campo será o identificador principal para login
    USERNAME_FIELD = 'usuario'

    def __str__(self):
        return self.usuario

class Categoria(models.Model):

    nome = models.CharField(max_length=150, unique=True)

    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.nome

class Tecnologia(models.Model):

    nome = models.CharField(max_length=150, unique=True)

    logo = models.ImageField(upload_to='static/images/technologies/', null=True, blank=True)

    link = models.URLField(max_length=200, blank=True)

class Projeto(models.Model):

    #ENUM SITUACOES DO PROJETO
    class Status(models.TextChoices):
        ATIVO ="ATIVO", "Ativo"
        FINALIZADO="FINALIZADO", "Finalizado"
        SUSPENSO ="SUSPENSO", "Suspenso"
        DESENVOLVIMENTO="DESENVOLVIMENTO", "Desenvolvimento"
        PLANEJAMENTO ="PLANEJAMENTO", "Planejamento"

    #nome
    nome = models.CharField(max_length=150, unique=True)

    #publico
    publico = models.BooleanField(default=False)

    #inicio
    inicio = models.DateField()

    #fim
    fim = models.DateField()

    #status (ativo, finalizado, suspenso,desenvolvimento,planejamento)
    status = models.CharField(
        max_length=12,
        choices=Status.choices,
        default= Status.PLANEJAMENTO
    )

    descricao = models.TextField()

    #categoria, foreign key -> categoria
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    #tecnologias, many-to-many -> tecnologia
    tecnologias = models.ManyToManyField(Tecnologia)

    #imagem
    imagem = models.ImageField(upload_to='static/images/projects/', null=True, blank=True)

    #github como URLFIELD para https://
    github = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.nome

class Membro(models.Model):
    # Enum para situacao de membros do pet
    class Situacao(models.TextChoices):
        BOLSISTA= "BOLSISTA", "Bolsista"
        NAO_BOLSISTA = "NAO_BOLSISTA", "Não-Bolsista"
        COLABORADOR = "COLABORADOR", "Colaborador"
        EX_MEMBRO = "EX_MEMBRO" , "Ex-membro"
    
    # nome do membro (separado do usuário que é utilizado para logar)
    nome = models.CharField(max_length=150)

    #foto como imagefield tratado pelo pillow e salvado no diretório static/images/membros/
    foto = models.ImageField(upload_to='static/images/membros/', null=True, blank=True)

    # link do github definido como URLFIELD para tratar com https:// 
    github = models.URLField(max_length=200, blank=True)

    # utilizando o enum para definir a situacao do membro
    situacao = models.CharField(
        max_length=12,
        choices=Situacao.choices,
        default= Situacao.COLABORADOR
    )

    descricao = models.TextField()

    #projetos many-to-many ->PROJETO
    projetos = models.ManyToManyField(Projeto)

    def __str__(self):
        return self.nome
    

class Atividade(models.Model):

    titulo= models.CharField(max_length=150, unique=True)

    descricao = models.TextField()

    data = models.DateField()

    horas = models.IntegerField()

    minutos = models.IntegerField()

    membros = models.ManyToManyField(Membro)

    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

class Etapa(models.Model):

    ordem = models.IntegerField()

    titulo = models.CharField(max_length=150, unique=True)

    descricao = models.TextField()
    inicio = models.DateTimeField()

    fim = models.DateTimeField()

    mostrar_hora = models.BooleanField(default=False)

    data_resultado = models.DateField()


class Processo(models.Model):

    class Semestre(models.IntegerChoices):
        PRIMEIRO=1, '1'
        SEGUNDO=2, '2'

    ano = models.IntegerField()

    ativo = models.BooleanField(default=False)

    semestre = models.IntegerField(
        choices = Semestre.choices,
        default = Semestre.SEGUNDO
    )

    vagas_bolsista = models.IntegerField()

    vagas_nao_bolsista = models.IntegerField()

    vagas_colaborador = models.IntegerField()

    inicio_inscricao = models.DateField()

    fim_inscricao = models.DateField()

    etapas = models.ManyToManyField(Etapa)

    email = models.EmailField()

    # salva em pastas organizadas por ano/mes, ex: static/edital/2026/03/edital.pdf
    edital = models.FileField(upload_to='static/edital/%Y/%m')

