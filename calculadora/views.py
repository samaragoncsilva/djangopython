from django.shortcuts import render

def index(request):
    resultado = None
    
    if request.method == "POST":
        num1 = float(request.POST.get("num1"))
        num2 = float(request.POST.get("num2"))
        operacao = request.POST.get("operacao")
        
        if operacao == "soma":
            resultado = num1 + num2
        elif operacao == "subtracao":
            resultado = num1 - num2
        elif operacao == "multiplicacao":
            resultado = num1 * num2
        elif operacao == "divisao":
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Erro: divisão por 0"
            
    return render(request, "calculadora/index.html", {"resultado": resultado})


# Create your views here.
