from django import forms
from cadastro_pet.models import CadastroAnimal
from .models import Adotante  # Certifique-se de que o caminho esteja correto

# Formulário para cadastro de animais
class PetForm(forms.ModelForm):
    class Meta:
        model = CadastroAnimal
        fields = "__all__"
        exclude = ['data_criacao', 'disponivel']

# Formulário para cadastro de adotantes
class AdotanteForm(forms.ModelForm):
    class Meta:
        model = Adotante
        fields = ['nome', 'cpf', 'telefone', 'email', 'pet']
        
    def __init__(self, *args, **kwargs):
        super(AdotanteForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'placeholder': 'Nome Completo'})
        self.fields['cpf'].widget.attrs.update({'placeholder': 'CPF (somente números)'})
        self.fields['telefone'].widget.attrs.update({'placeholder': 'Telefone'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['pet'].empty_label = "Selecione um Pet"  # Customiza a label do campo de seleção
    
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        # Adicione lógica para verificar se o CPF já está cadastrado, se necessário
        return cpf


