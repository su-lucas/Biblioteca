from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    classificacao_indicativa = models.IntegerField(default=0)

    def __str__(self):
        return self.nome