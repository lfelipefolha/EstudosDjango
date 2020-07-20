from django.shortcuts import render
from .models import Produtos
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    produtos = Produtos.objects.all()
    context = { 'outro':'Ainda não me chame de bb',
                'curso':'meu amigo da escola é um macaco ',
                'produtos':produtos}
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    #prod = Produtos.objects.get(id=pk)
    prod = get_object_or_404(Produtos, id=pk)

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
