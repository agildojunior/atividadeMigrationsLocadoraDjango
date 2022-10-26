import email
from http import client
from msilib.schema import Class
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

class Filme(models.Model):
    titulo = models.CharField(max_length=50)
    data_lancamento = models.DateTimeField()
    valor_locacao = models.FloatField()
    Categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

class Locacao(models.Model):
    data_entrega = models.DateTimeField()
    data_locacao = models.DateTimeField()
    valor = models.FloatField()
    Cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    Filme = models.ForeignKey(Filme, on_delete=models.PROTECT)