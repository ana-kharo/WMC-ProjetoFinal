from django.shortcuts import render, get_object_or_404

from cadastro_pet.models import CadastroAnimal


def detalhe_animal(request, animal_id):
    # Busca o animal pelo ID, ou retorna 404 se não for encontrado
    animal = get_object_or_404(CadastroAnimal, id=animal_id)
    
    # Renderiza o template e passa o objeto `animal` como contexto
    return render(request, 'detalhes_pet.html', {'animal': animal})