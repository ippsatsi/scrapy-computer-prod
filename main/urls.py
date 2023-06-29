from django.urls import path
from .views import ListaProductos, BuscarProductos

urlpatterns = [
   # path("", Home.as_view(), name="home"),
    path("", ListaProductos.as_view(), name="lista_productos"),
    path("buscar/", BuscarProductos.as_view(), name="buscar_productos"),
]