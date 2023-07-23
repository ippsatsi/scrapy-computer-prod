from django.urls import path
from .views import ListaProductos, BuscarProductos, ListaProductosProveedor

urlpatterns = [
   # path("", Home.as_view(), name="home"),
    path("", ListaProductos.as_view(), name="lista_productos"),
    path("buscar/", BuscarProductos.as_view(), name="buscar_productos"),
    path("proveedor/", ListaProductosProveedor.as_view(), name="lista_productosxproveedor"),
]