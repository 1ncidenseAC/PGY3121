from django.shortcuts import render
from .models import Producto, Categoria

# Create your views here.

def index(request):
    return render(request, 'web/index.html')

def ofertas(request):
    return render(request, 'web/ofertas.html')

def perros(request):
    return render(request, 'web/perros.html')

def gatos(request):
    return render(request, 'web/gatos.html')

def accesorios(request):
    return render(request, 'web/accesorios.html')

def mod(request):
    mod = Producto.objects.all()
    context = {"mod": mod}
    return render(request, 'web/mod.html', context)