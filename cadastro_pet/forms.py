'''
Classe do formulario => define quais campos vamos validar.
Field => campo do formulário, isto é, qual é o tipo do campo (senha, e-mail, nome, etc).
Widget => como o campo vai ser representado em HTML (input, text area, etc.)
'''

#Importamos do Django o Forms.
from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ['id', 'data_criacao']

        labels = {
            'nome_pet': 'Nome',
            'idade_pet': 'Idade',
            'raca_pet': 'Raça',
            'imagem': 'Imagem',
            'especie_pet': 'Espécie',
            'historico_saude': 'Histórico de Saúde',
        }
