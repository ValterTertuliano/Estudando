from django.http import HttpResponse

# from django.shortcuts import render


# Create your views here.
def blogapp(request):  # recebe uma requisição como parametro
    # dentro do bloco posso fazer outras coisas
    return HttpResponse(
        "Olá Mundo !!! -- Isso é uma view - do app blog"
    )  # resposta para o cliente
