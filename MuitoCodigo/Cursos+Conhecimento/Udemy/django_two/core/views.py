from django.shortcuts import render
from .forms import Contato
from django.shortcuts import redirect


def index(request):
    form = Contato(request.POST)
    if form.is_valid():
        form.send_email()

        return redirect('index')
    else:
        form = Contato()

    return render(request, 'index.html', {'form': form})
