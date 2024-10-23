from django.urls import path

from . import views

urlpatterns = [
    path("cadastro_animal/", views.cadastro, name="cadastro_animal"),
]