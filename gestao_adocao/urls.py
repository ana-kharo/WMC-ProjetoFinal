from django.urls import path
from .views import listar_adocoes, criar_adocao, editar_adocao, remover_adocao, adote_view

urlpatterns = [
    path('adote/', listar_adocoes, name='listar_adocao'),
    path('adote/cadastrar/', criar_adocao, name='cadastrar_adocao'), 
    path('adote/editar/<int:id>/', editar_adocao, name='editar_adocao'),  
    path('adote/remover/<int:id>/', remover_adocao, name='remover_adocao'), 
    path('', adote_view, name='adote'),
]


