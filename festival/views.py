from django.shortcuts import get_object_or_404, redirect, render
from .models import Dia, Palco, Concerto, Banda             
from .forms import ConcertoForm, PalcoForm


def index_view(request):
    return render(request, 'festival/index.html')

def dias_view(request):
    dias = Dia.objects.all().order_by('data')

    context = {'dias': dias}

    return render(request, 'festival/dias.html', context)


def palcos_view(request):
    palcos = Palco.objects.all() 

    context = {'palcos': palcos}

    return render(request, 'festival/palcos.html', context)


def concerto_view(request, concerto_id):
    concerto = Concerto.objects.get(id=concerto_id)

    context = {'concerto': concerto}

    return render(request, 'festival/concerto.html', context)


def editar_concerto_view(request, concerto_id):
    concerto = get_object_or_404(Concerto, id=concerto_id)

    if request.method == 'POST':
        form = ConcertoForm(request.POST, instance=concerto)
        if form.is_valid():
            form.save()
            return redirect('concerto', concerto_id=concerto.id)
    else:
        form = ConcertoForm(instance=concerto)

    context = {
        'concerto': concerto,
        'form': form,
    }

    return render(request, 'festival/editar_concerto.html', context)

def apagar_concerto_view(request, concerto_id):
    concerto = get_object_or_404(Concerto, id=concerto_id)

    if request.method == 'POST':
        concerto.delete()
        return redirect('dias')

    context = {
        'concerto': concerto,
    }

    return render(request, 'festival/concerto_apagar.html', context)

def criar_concerto_view(request):
    form = ConcertoForm(request.POST or None)

    if request.method == 'POST':
        print(f"Request method: {request.method}")
        print(f"Form is valid: {form.is_valid()}")
        print(f"Form errors: {form.errors}")
        print(f"POST data: {request.POST}")
        if form.is_valid():
            concerto = form.save()
            return redirect('concerto', concerto_id=concerto.id)
    else:
        form = ConcertoForm()

    context = {
        'form': form,
    }

    bandas = Banda.objects.all().order_by('nome')
    palcos = Palco.objects.all().order_by('nome')
    dias = Dia.objects.all().order_by('data')
    return render(request, 'festival/concerto_criar.html', {'bandas': bandas, 'palcos': palcos, 'dias': dias, 'form': form, 'action': 'Create'})
