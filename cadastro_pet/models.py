from django.utils import timezone
import uuid
from django.db import models

class Pet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    nome_pet = models.CharField(max_length=50, blank=False) 
    idade_pet = models.CharField(max_length=20, blank=False)
    raca_pet = models.CharField(max_length=30, blank=False)
    imagem = models.ImageField(upload_to='imagens/')  
    data_criacao = models.DateTimeField(auto_now_add=True)
    adotado = models.BooleanField(default=False)

    ESPECIES_CHOICES = [
        ("gato", "Gato"),
        ("cachorro", "Cachorro"),
    ]
    
    especie_pet = models.CharField(max_length=10, choices=ESPECIES_CHOICES, blank=False)  

    historico_saude = models.TextField(blank=True)  

    def __str__(self):
        return f'{self.id}, {self.nome_pet}, {self.imagem}'

    class Meta:
        verbose_name = 'Formulário Novo Pet'
        verbose_name_plural = 'Formulários de pets'
        ordering = ['data_criacao']