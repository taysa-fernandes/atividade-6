from django.contrib import admin
from django.urls import path
from core.views import lista_discos, detalhes_disco, cadastrar_disco, editar_disco, excluir_disco

urlpatterns = [
    path('admin/', admin.site.urls),
    path('discos/', lista_discos, name='lista_discos'),
    path('discos/<int:disco_id>/', detalhes_disco, name='detalhes_disco'),
    path('discos/cadastro/', cadastrar_disco, name='cadastro_disco'),
    path('discos/editar/<int:disco_id>/', editar_disco, name='editar_disco'),
    path('discos/excluir/<int:disco_id>/', excluir_disco, name='excluir_disco'),
]
