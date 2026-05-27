from django.db import models

class ConfiguracaoSite(models.Model):

    imagem_fundo = models.ImageField(
        upload_to="fundos_site/", 
        null=True, 
        blank=True
    )

    class Meta:
        verbose_name = "Configuração do Site"
        verbose_name_plural = "Configurações do Site"

    def __str__(self):
        return "Configurações"

class Categoria(models.Model):

    nome = models.CharField(max_length=150, unique=True)

    slug = models.SlugField(max_length=150)

    interna = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Tecnologia(models.Model):

    nome = models.CharField(max_length=150, unique=True)

    logo = models.ImageField(upload_to='tecnologias_logos/', null=True, blank=True)

    link = models.URLField(max_length=200, blank=True)

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
    sobrenome = models.CharField(max_length=150, blank=True)

    #foto como imagefield
    foto = models.ImageField(upload_to='membros_fotos/', null=True, blank=True)
    capa = models.ImageField(upload_to='membros_capas/', null=True, blank=True)

    # link do github definido como texto
    github = models.CharField(max_length=50, blank=True)

    # link do linkedin definido como texto
    linkedin = models.CharField(max_length=200, blank=True)

    # utilizando o enum para definir a situacao do membro
    situacao = models.CharField(
        max_length=12,
        choices=Situacao.choices,
        default= Situacao.COLABORADOR
    )

    descricao = models.TextField()

    class Meta:
        ordering = ["nome", "sobrenome"]

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

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

    #descrição
    descricao = models.TextField()

    #inicio
    data_inicio = models.DateField()

    #fim
    data_fim = models.DateField(null=True, blank=True)

    #imagem
    imagem = models.ImageField(upload_to='projetos_fotos/', null=True, blank=True)

    #publico
    publico = models.BooleanField(default=False)

    #github como URLFIELD para https://
    github = models.URLField(max_length=200, blank=True)

    #status (ativo, finalizado, suspenso, desenvolvimento, planejamento)
    status = models.CharField(
        max_length=15,
        choices=Status.choices,
        default= Status.PLANEJAMENTO
    )

    #categoria, foreign key -> categoria
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    #tecnologias, many-to-many -> tecnologia
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)

    #membros, many-to-many -> membro
    membros = models.ManyToManyField(
        Membro,
        related_name="projetos",
        blank=True
    )

    def __str__(self):
        return self.nome


class Atividade(models.Model):

    titulo= models.CharField(max_length=150)

    descricao = models.TextField()

    data = models.DateField()

    horas = models.IntegerField()

    minutos = models.IntegerField()

    membros = models.ManyToManyField(Membro)

    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.projeto.nome}] {self.titulo}"

    def get_hora_formatada(self):
        minutos_totais = self.horas * 60 + self.minutos

        horas = minutos_totais // 60
        mins = minutos_totais % 60

        if horas and mins:
            return f"{horas}h{mins:02d}min"
        elif horas:
            return f"{horas}h"
        else:
            return f"{mins}min"

class Etapa(models.Model):

    ordem = models.IntegerField()

    titulo = models.CharField(max_length=150, unique=True)

    descricao = models.TextField()

    data_inicio = models.DateField()
    hora_inicio = models.TimeField(null=True, blank=True)

    data_fim = models.DateField()
    hora_fim = models.TimeField(null=True, blank=True)

    data_resultado = models.DateField(null=True, blank=True)
    hora_resultado = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"Etapa {self.ordem} - {self.titulo}"


class ProcessoSeletivo(models.Model):

    class Semestre(models.IntegerChoices):
        PRIMEIRO=1, '1'
        SEGUNDO=2, '2'

    ano = models.IntegerField()

    ativo = models.BooleanField(default=True)

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

    # salva em pastas organizadas por ano/mes
    edital = models.FileField(upload_to='editais/')

    formulario = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"Processo Seletivo - {self.ano}/{self.semestre}"
    

