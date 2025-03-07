from django.shortcuts import render
from . import forms


def index(request):
    return render(request, 'index.html')


def contato(request):
    form = forms.ContatoForm()
    context = {
        'form': form,
    }

    return render(request, 'contato.html', context)


def produto(request):
    return render(request, 'produto.html')
