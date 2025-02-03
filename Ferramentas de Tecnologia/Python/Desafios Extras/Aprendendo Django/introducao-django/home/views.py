from django.shortcuts import render


# Create your views here.
# blog e my_view são views baseadas em funções, tendo dois tipos
# a segunda forma de view é de classes
def homeapp(request):
    print(
        "Essa é a HOME da pagina que esta dentro do app home-views\
    Adicionado arquivo urls dentro da pasta do app, para criação de urls aninhadas"
    )
    return render(request, "home.html")
