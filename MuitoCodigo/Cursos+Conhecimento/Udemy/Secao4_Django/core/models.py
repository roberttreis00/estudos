from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    estoque = models.IntegerField()
