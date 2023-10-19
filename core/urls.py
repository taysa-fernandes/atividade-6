from django.contrib import admin
from django.urls import path
from  core.views import lista_discos, detalhes_disco

urlpatterns = [
    path('discos/',lista_discos, name='lista_discos'),
    path('discos/<int:disco_id>/',detalhes_disco, name='detalhes_disco'),
]