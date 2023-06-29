from django.shortcuts import render
from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.db.models import Q
from functools import reduce
from datetime import date

from .models import Quote, Producto
# Create your views here.


class ListaProductos(ListView):
    model = Producto
    paginate_by = 100
    ordering = "-marca"
    template_name = "buscador.html"

    def get_queryset(self):
        result_delete = Producto.objects.filter(fecha__lt=date.today()).delete()
        print(result_delete)
        return Producto.objects.order_by('-marca', '-precio_soles')

class BuscarProductos(ListView):
    model = Producto
    ordering = "-marca"
    paginate_by = 30
    template_name = "buscador.html"

    def get_queryset(self):
        list_query = self.request.GET.get("q").split()
        str_query = reduce(
            lambda a, b: a & b,
            (Q(titulo__icontains=term) for term in list_query),
        )
        return Producto.objects.filter(str_query).order_by('-marca', '-precio_soles')
    