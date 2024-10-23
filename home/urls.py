from django.urls import path
from . import views  # Certifique-se de que você está importando suas views corretamente

urlpatterns = [
    path('', views.home, name='index'),  # Exemplo de rota
]