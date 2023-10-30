from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Sebo_discos
from .forms import DiscoForm

def lista_discos(request):
    discos = Sebo_discos.objects.all()
    return render(request, 'core/lista_discos.html', {'discos': discos})

def detalhes_disco(request, disco_id):
    disco = get_object_or_404(Sebo_discos, pk=disco_id)
    return render(request, 'core/detalhes_disco.html', {'disco': disco})

def cadastrar_disco(request):
    if request.method == 'POST':
        form = DiscoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_discos')
    else:
        form = DiscoForm()
    return render(request, 'core/cadastro_disco.html', {'form': form})

def editar_disco(request, disco_id):
    disco = get_object_or_404(Sebo_discos, pk=disco_id)
    if request.method == 'POST':
        form = DiscoForm(request.POST, instance=disco)
        if form.is_valid():
            form.save()
            return redirect('lista_discos')
    else:
        form = DiscoForm(instance=disco)
    return render(request, 'core/editar_disco.html', {'form': form, 'disco': disco})

def excluir_disco(request, disco_id):
    disco = get_object_or_404(Sebo_discos, pk=disco_id)
    if request.method == 'POST':
        disco.delete()
        return redirect('lista_discos')
    return render(request, 'core/excluir_disco.html', {'disco': disco})
