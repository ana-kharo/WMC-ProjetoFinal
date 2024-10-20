from django.shortcuts import render
import requests

def pets_lista(request):
    response = requests.get('http://127.0.0.1:8000/api/pet')  # URL da sua API
    pets = response.json() if response.status_code == 200 else []
    print(pets)  # Adicione esta linha para verificar a resposta

    context = {
        'pets': pets,
    }
    return render(request, 'home.html', context)

def home(request):
    response = requests.get('http://127.0.0.1:8000/api/pet')  # URL da sua API
    pets = response.json() if response.status_code == 200 else []
    print(pets)  # Adicione esta linha para verificar a resposta

    context = {
        'pets': pets,
    }

    return render(request, 'home.html', context)
