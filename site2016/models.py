from django.db import models
import datetime
from django.conf import settings

class MembroEquipe(models.Model):

    class Meta:
        verbose_name = 'membro de equipe'
        verbose_name_plural = 'membros da equipe'

    def __str__(self):
        return self.nome + ' ' + self.sobrenome

    ANO_CHOICES = [(i, i) for i in range(2006, datetime.datetime.now().year)]

    nome = models.CharField(max_length=50, verbose_name='nome')
    sobrenome = models.CharField(max_length=100, verbose_name='sobrenome')
    ano = models.IntegerField(verbose_name='ano', blank=True, choices=ANO_CHOICES)
    foto = models.ImageField(verbose_name='foto', blank=True, upload_to='images/equipe/')
    github = models.CharField(max_length=100, blank=True, verbose_name='GitHub')


class Aluno(MembroEquipe):
    class Meta:
        verbose_name = 'aluno'
        verbose_name_plural = 'alunos'

    def __str__(self):
        return '[Aluno] ' + self.nome + ' ' + self.sobrenome

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
