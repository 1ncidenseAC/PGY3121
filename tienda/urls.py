from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ofertas', views.ofertas, name='ofertas'),
    path('perros', views.perros, name='perros'),
    path('gatos', views.gatos, name='gatos'),
    path('accesorios', views.accesorios, name='accesorios'),
    path('mod', views.mod, name='mod'),
]