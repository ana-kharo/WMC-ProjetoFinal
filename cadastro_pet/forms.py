'''
Classe do formulario => define quais campos vamos validar.
Field => campo do formulário, isto é, qual é o tipo do campo (senha, e-mail, nome, etc).
Widget => como o campo vai ser representado em HTML (input, text area, etc.)
'''
from django import forms

from cadastro_pet.models  import CadastroAnimal

class PetForm(forms.ModelForm):
    class Meta:
        model = CadastroAnimal
        fields = "__all__"
        exclude = ['data_criacao', 'disponivel']
