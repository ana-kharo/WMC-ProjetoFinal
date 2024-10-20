from django.shortcuts import render
import requests


def home(request):
    response = requests.get('http://127.0.0.1:8000/api/pet')  
    pets = response.json() if response.status_code == 200 else []
    print(pets)  

    context = {
        'pets': pets,
    }

    return render(request, 'home.html', context)
