from django.shortcuts import render
from datetime import datetime

def index(request):
    resultado = None
    if request.method == 'POST':
        nome = request.POST.get('nome', '').upper()
        ano_nasc = int(request.POST.get('ano_nasc', 0))
        ano_atual = datetime.now().year
        idade = ano_atual - ano_nasc
        
        # Mover toda a lógica para DENTRO do if POST
        if idade < 18:
            resultado = f'{nome} você ainda tem {idade} anos, não tem idade suficiente para se alistar'.upper()
        elif idade == 18:
            resultado = f'{nome}, você já tem {idade} anos, precisa se alistar.'.upper()
        else:
            resultado = f'{nome}, você já tem {idade} anos, está atrasado com o seu alistamento.'.upper()

    return render(request, 'alistamento/index.html', {'resultado': resultado})