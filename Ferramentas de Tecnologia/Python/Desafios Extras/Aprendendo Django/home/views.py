from django.http import HttpResponse

# from django.shortcuts import render


# Create your views here.
# blog e my_view são views baseadas em funções, tendo dois tipos
# a segunda forma de view é de classes
def homeapp(request):
    return HttpResponse("Essa é a HOME da pagina que esta dentro do app home-views")
