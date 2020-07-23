from .models import Paciente
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from .forms import PacienteModelForm
# Create your views here.

def index(request):

    return render(request, 'index.html')
def cadastro(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = PacienteModelForm(request.POST)
            if form.is_valid():

                form.save()

                messages.success(request, 'Produto salvo com sucesso.')
                form = PacienteModelForm()
            else:
                messages.error(request, 'Erro ao salvar produto.')
        else:
            form = PacienteModelForm()
        context = {
            'form': form
        }
        return render(request, 'cadastro.html', context)
    else:
        return redirect('index')


def alteracao(request):
    return render(request, 'alteracao.html')

def listagem(request):
        context = {
            'pacientes': Paciente.objects.all()
        }
        return render(request, 'listagem.html', context)

def exclusao(request):
    return render(request, 'exclusao.html')


def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)