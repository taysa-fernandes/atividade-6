from django.shortcuts import render, get_object_or_404
from .models import Sebo_discos

def lista_discos(request):
    discos = Sebo_discos.objects.all()
    return render(request, 'core/lista_discos.html', {'discos': discos})

def detalhes_disco(request, disco_id):
    disco = get_object_or_404(Sebo_discos, pk=disco_id)
    return render(request, 'core/detalhes_disco.html', {'disco': disco})
