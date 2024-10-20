from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from cadastro_pet.models import Pet
from rest_api.serializers import PetSerializer 

# Create your views here.

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data.get("name")}'})
    return Response({'hello': 'World API'})

class PetModelViewSet(ModelViewSet):
    queryset  = Pet.objects.all()
    serializer_class = PetSerializer
