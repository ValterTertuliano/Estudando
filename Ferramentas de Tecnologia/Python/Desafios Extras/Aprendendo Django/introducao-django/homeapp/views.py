from django.shortcuts import render

# Create your views here.


# isso é uma view para a pagina inicial
def home(request):
    print(
        "Pagina inicial - mudei para pasta homeapp - url aninhada - mudando http para render para renderizar html",
        "home.html",
    )
    return render(request, "homeapp/home.html")
