from django.shortcuts import render


# Create your views here.
def blogapp(request):  # recebe uma requisição como parametro
    # dentro do bloco posso fazer outras coisas
    print(
        "Olá Mundo !!! -- Isso é uma view - do app blog - Adicionado arquivo urls dentro da pasta do app, para criação de urls aninhadas"
    )
    return render(request, "blog.html")  # resposta para o cliente


def exemplo_url_aninhada(request):
    print("Esse é um exemplo de aninhamento de rotas... das rotas 'BLOG' ")
    return render(request, "blogexemplo.html")
