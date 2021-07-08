from django.urls.conf import path
import produto
from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto, Categoria, Opcoes, Adicional


def home(request):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'home.html', {'produtos': produtos,
                                        'carrinho': len(request.session['carrinho']),
                                        'categorias': categorias,
                                        })
                                
def categoria(request, id):
    produtos = Produto.objects.filter(categoria_id = id)
    categorias = Categoria.objects.all()

    return render (request, 'home.html', {
        'produtos':produtos,
        'carrinho': len(request.session['carrinho']),
        'categorias':categorias
    })

def produto(request, id):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    erro = request.GET.get('erro')
    produto = Produto.objects.filter(id=id)[0]
    categorias = Categoria.objects.all()
    
    return render(request, 'produto.html', {
        'produto':produto,
        'carrunho': len(request.session['carrinho']),
        'categorias':categorias,
        'erro':erro
    })