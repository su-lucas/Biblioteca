from django.db import models

# Create your models here.
from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField(null=True, blank=True)
    ganhador_premio = models.BooleanField(default=False)

    def __str__(self):
        return self.nome