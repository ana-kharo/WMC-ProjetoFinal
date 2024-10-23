from django.shortcuts import render

from cadastro_pet.models import CadastroAnimal

def home(request):
    animais = CadastroAnimal.objects.filter(disponivel = True)
    
    return render(request, 'home.html', {'animais': animais})
