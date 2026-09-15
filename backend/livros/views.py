# Create your views here.
from django.http import JsonResponse
from .models import Livro

def listar_livros(request):
    livros = Livro.objects.all()
    lista_dados = []
    
    for livro in livros:
        lista_dados.append({
            'id': livro.id,
            'titulo': livro.titulo,
            'ano_publicacao': livro.ano_publicacao,
            'disponivel': livro.disponivel,
            'autor': livro.autor.nome if livro.autor else 'Desconhecido'
        })
        
    return JsonResponse({'livros': lista_dados})