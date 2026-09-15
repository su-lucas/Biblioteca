
from django.db import models
from autores.models import Autor

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    ano_publicacao = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    
    # requisito 3: relacionamento ForeignKey (1:N)
    #nesse caso a relação é de 1:N, pois um autor pode ter vários livros, mas cada livro pertence a apenas um autor.
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livros')

    def __str__(self):
        return self.titulo