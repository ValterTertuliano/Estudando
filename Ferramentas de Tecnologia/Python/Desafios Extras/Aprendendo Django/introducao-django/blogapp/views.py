from django.shortcuts import render


# Create your views here.
# isso é uma view para a rota blog
def blog(request):
    print("Essa é a view da blog - mudei para pasta blogapp - url aninhada")
    return render(request, "blogapp/blog.html")


def exemploblog(request):
    print("essa é uma view de uma url aninhada com blog - ")
    return render(request, "blogapp/exemplo.html")
