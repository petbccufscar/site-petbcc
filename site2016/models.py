from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
import datetime


class MembroEquipe(models.Model):
    class Meta:
        verbose_name = 'membro de equipe'
        verbose_name_plural = 'membros da equipe'

    def __str__(self):
        return self.nome + ' ' + self.sobrenome

    ANO_CHOICES = [(i, i) for i in range(2006, datetime.datetime.now().year)]

    nome = models.CharField(max_length=50, verbose_name='nome')
    sobrenome = models.CharField(max_length=100, verbose_name='sobrenome')
    ano = models.IntegerField(verbose_name='ano', null=True, blank=True, choices=ANO_CHOICES)
    foto = models.ImageField(verbose_name='foto', null=True, blank=True, upload_to='images/equipe/')
    github = models.CharField(max_length=100, null=True, blank=True, verbose_name='GitHub')


class Aluno(MembroEquipe):
    class Meta:
        verbose_name = 'aluno'
        verbose_name_plural = 'alunos'

    def __str__(self):
        situacao_aluno = {
            'B': 'Bolsista',
            'N': 'Não-bolsista',
            'V': 'Voluntário',
            'E': 'Ex-membro'
        }
        return '[' + situacao_aluno[self.situacao] + '] ' + self.nome + ' ' + self.sobrenome

    SITUACAO_CHOICES = (
        ('B', 'Bolsista'),
        ('N', 'Não-bolsista'),
        ('V', 'Voluntário'),
        ('E', 'Ex-membro')
    )

    situacao = models.CharField(max_length=1, choices=SITUACAO_CHOICES, verbose_name='situação no PET')


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

    titulo = models.CharField(max_length=10, verbose_name='título', blank=True, choices=TITULO_CHOICES)
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

    data_inicio = models.DateTimeField(verbose_name="data inicial", blank=True, null=True)
    data_fim = models.DateTimeField(verbose_name="data final", blank=True, null=True)

    mostrar_hora = models.BooleanField(verbose_name="mostrar hora", default=False)

    resultado = models.TextField(verbose_name="resultado", blank=True, null=True)

    data_resultado = models.DateField(verbose_name="data do resultado", null=True)

    mostrar_resultado = models.BooleanField(verbose_name="mostrar resultado", default=False)


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

    vagas_bolsistas = models.PositiveIntegerField(
        verbose_name="vagas bolsistas",
        default=12
    )

    vagas_nao_bolsistas = models.PositiveIntegerField(
        verbose_name="vagas não bolsistas",
        default=6
    )

    data_inscricao_inicio = models.DateField(verbose_name="data inicial de inscrição")
    data_inscricao_fim = models.DateField(verbose_name="data final de inscrição")

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
