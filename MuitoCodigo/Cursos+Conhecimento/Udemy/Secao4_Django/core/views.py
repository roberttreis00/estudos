from django.shortcuts import render
from . forms import ContatoForm


def index(request):
    form = ContatoForm()

    return render(request, 'index.html', {'form': form})
