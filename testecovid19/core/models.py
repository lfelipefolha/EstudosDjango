from django.db import models

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Paciente(Base):

    TESTE_CHOICES = (
        ('ertpcr','ERT-PCR'),
        ('sorologia','ERT-PCR'),
        ('testerapidoatg','Teste Rápido - Antígenos'),
        ('testerapidoatc','Teste Rápido - Anticorpos'),
    )
    RES_CHOICES =(
        ('positivo','Positivo'),
        ('negativo', 'Negativo'),
    )
    nome = models.CharField('Nome', max_length=100)
    dnasc = models.DateField('Data de nacimento')
    email = models.EmailField(max_length=100)
    typeteste = models.CharField('Tipo do teste', max_length=100, choices=TESTE_CHOICES)
    resteste = models.CharField('Resultado', max_length=100, choices=RES_CHOICES)
    def __str__(self):
        return self.nome


