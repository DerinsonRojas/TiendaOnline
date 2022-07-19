from django.http import HttpResponse
from django.shortcuts import render
from gestionPedidos.models import Articulos


def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):

    if request.GET["prd"]:
        #mensaje="Artículo buscado: %r"%request.GET["prd"]
        producto=request.GET["prd"]

        articulos=Articulos.objects.filter(nombre__icontains=producto)

        return render (request, "resultados_busqueda.html",{"articulos":articulos, "query":producto})
    else:

        mensaje="No has introducido nada"

    return HttpResponse(mensaje)
# Create your views here.
