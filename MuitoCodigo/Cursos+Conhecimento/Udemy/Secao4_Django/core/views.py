from django.shortcuts import render, redirect
from . forms import ContatoForm, ProdutoModelForm
from . models import Produto


def index(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST)
        if form.is_valid():

            form.save()
            # Salvo no banco

        return redirect('index')
    else:
        form = ProdutoModelForm()

    return render(request, 'index.html', {'form': form})
