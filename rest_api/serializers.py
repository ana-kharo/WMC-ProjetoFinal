import uuid 
from rest_framework import serializers
from cadastro_pet.models import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        exclude = ['data_criacao'] 

    def create(self, validated_data):
        validated_data['id'] = str(uuid.uuid4()) 
        return super().create(validated_data)
