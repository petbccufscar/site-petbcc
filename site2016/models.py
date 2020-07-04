from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

import datetime

class MembroEquipeManager(models.Manager):
    def listar_membros_ativos(self):
        return super().get_queryset().exclude(situacao='E')

    def listar_bolsistas(self):
        return super().get_queryset().filter(situacao='B')

    def listar_nao_bolsistas(self):
        return super().get_queryset().filter(situacao='N')

    def listar_colaboradores(self):
        return super().get_queryset().filter(situacao='V')

    def listar_ex_membros(self):
        return super().get_queryset().filter(situacao='E')


class MembroEquipe(models.Model):
    class Meta:
        verbose_name = 'membro de equipe'
        verbose_name_plural = 'membros da equipe'

    def __str__(self):
        situacao = {
            'B': 'Bolsista',
            'N': 'Não-bolsista',
            'V': 'Colaborador',
            'E': 'Ex-membro'
        }
        return "["+situacao[self.situacao]+"] "+self.nome + ' ' + self.sobrenome

    objects = MembroEquipeManager()

    nome = models.CharField(max_length=50, verbose_name='nome')
    sobrenome = models.CharField(max_length=100, verbose_name='sobrenome')
    foto = models.ImageField(
        verbose_name='foto', null=True, blank=True, upload_to='images/equipe/')
    github = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='GitHub')

    SITUACAO_CHOICES = (
        ('B', 'Bolsista'),
        ('N', 'Não-bolsista'),
        ('V', 'Colaborador'),
        ('E', 'Ex-membro')
    )

    situacao = models.CharField(
        max_length=1, choices=SITUACAO_CHOICES, verbose_name='situação no PET')


class Aluno(MembroEquipe):
    class Meta:
        verbose_name = 'aluno'
        verbose_name_plural = 'alunos'

    CURSO_CHOICES = (
        ('BCC', 'BCC'),
        ('EnC', 'EnC'),
        ('FIS', 'Física')
        )

    curso = models.CharField(
        max_length=5, verbose_name='curso', blank=True, choices=CURSO_CHOICES)

    ANO_CHOICES = [(i, i)
                   for i in range(2010, datetime.datetime.now().year + 1)]

    ano = models.IntegerField(
        verbose_name='ano', null=True, blank=True, choices=ANO_CHOICES)


class Professor(MembroEquipe):
    class Meta:
        verbose_name = 'professor'
        verbose_name_plural = 'professores'

    def __str__(self):
        return '[Professor] ' + self.nome + ' ' + self.sobrenome

    TITULO_CHOICES = (
        ('Dr.', 'Dr.'),
        ('Dr.ª', 'Dr.ª')
    )

    titulo = models.CharField(
        max_length=10, verbose_name='título', blank=True, choices=TITULO_CHOICES)
    descricao = models.CharField(max_length=250, verbose_name='descrição')
    email = models.EmailField(verbose_name='e-mail')


class EtapaPS(models.Model):
    class Meta:
        verbose_name = 'etapa'
        verbose_name_plural = 'etapas'

    def __str__(self):
        return '[' + str(self.ordem) + '] ' + self.titulo

    ordem = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )

    titulo = models.CharField(verbose_name="titulo", max_length=50)

    data_inicio = models.DateTimeField(
        verbose_name="data inicial", blank=False, null=False)
    data_fim = models.DateTimeField(
        verbose_name="data final", blank=True, null=True)

    mostrar_hora = models.BooleanField(
        verbose_name="mostrar hora", default=False)

    resultado = models.TextField(
        verbose_name="resultado", blank=True, null=True)

    data_resultado = models.DateField(
        verbose_name="data do resultado", blank=True, null=True)

    mostrar_resultado = models.BooleanField(
        verbose_name="mostrar resultado", default=False)


class ProcessoSeletivo(models.Model):
    class Meta:
        verbose_name = 'processo seletivo'
        verbose_name_plural = 'processos seletivos'

        unique_together = ("ano", "semestre")

    def __str__(self):
        return '[Processo Seletivo] ' + str(self.ano) + '/' + str(self.semestre)

    ano = models.IntegerField(
        verbose_name='ano',
        null=False,
        blank=False,
        default=datetime.datetime.now().year,
        validators=[
            MinValueValidator(2010)
        ]
    )

    ativo = models.BooleanField(verbose_name="PS ativo", default=True)

    semestre = models.IntegerField(
        verbose_name='semestre',
        null=False,
        blank=False,
        default=1 + datetime.datetime.now().month // 7,
        validators=[
            MinValueValidator(1)
        ]
    )

    vagas_bolsista = models.PositiveIntegerField(
        verbose_name="vagas bolsistas",
        default=12
    )

    vagas_nao_bolsista = models.PositiveIntegerField(
        verbose_name="vagas não bolsistas",
        default=6
    )

    data_inscricao_inicio = models.DateField(
        verbose_name="data inicial de inscrição")
    data_inscricao_fim = models.DateField(
        verbose_name="data final de inscrição")

    etapas = models.ManyToManyField(EtapaPS)

    requisitos = models.TextField(
        verbose_name="requisitos",
        default=' <li value="a)">Ser aluno regularmente matriculado no curso de Bacharelado em Ciência da '
                'Computação e estar cursando a partir do 2º (segundo) semestre de graduação; </li>\n'
                '<li value="b)">Apresentar média ponderada semestral geral maior ou igual a 6.0 (seis);</li>\n'
                '<li value="c)">Ter disponibilidade para se dedicar 20 (vinte) horas semanais nas atividades'
                'do programa;</li>')

    email_inscricao = models.EmailField(verbose_name="email para inscrição")
    edital = models.FileField(verbose_name="edital")


class Categoria_de_projeto(models.Model):
    class Meta:
        verbose_name = 'categoria de projeto'
        verbose_name_plural = 'categorias de projeto'

    def __str__(self):
        return '[' + self.sigla + '] ' + self.nome

    nome = models.CharField(verbose_name='nome', max_length=50)
    sigla = models.CharField(verbose_name='sigla', max_length=5)


class Tecnologia(models.Model):
    class Meta:
        verbose_name = 'tecnologia'
        verbose_name_plural = 'tecnologias'

    def __str__(self):
        return self.nome

    nome = models.CharField(verbose_name='nome', max_length=100)
    imagem = models.ImageField(verbose_name='logo', blank=True, null=True)
    link = models.CharField(verbose_name='link',
                            max_length=100, blank=True, null=True)


class Projeto(models.Model):
    class Meta:
        verbose_name = 'projeto'
        verbose_name_plural = 'projetos'

    def __str__(self):
        return self.nome

    nome = models.CharField(verbose_name='nome', max_length=100)

    STATUS_CHOICES = (
        ('D', 'Em desenvolvimento'),
        ('A', 'Ativo'),
        ('F', 'Finalizado'),
        ('S', 'Suspenso')
    )

    data_inicio = models.DateField(verbose_name="data de início", default=datetime.datetime.now, blank=True,
                                   null=True)
    data_final = models.DateField(
        verbose_name="data de finalização", blank=True, null=True)

    status = models.CharField(verbose_name='status do projeto',
                              choices=STATUS_CHOICES, max_length=1, default='A')

    descricao = models.TextField(verbose_name='descrição')

    tecnologias = models.ManyToManyField(
        Tecnologia, verbose_name='tecnologias utilizadas', blank=True)

    categorias = models.ManyToManyField(
        Categoria_de_projeto, verbose_name='categorias do projeto')

    imagem = models.ImageField(verbose_name="imagem do projeto")
