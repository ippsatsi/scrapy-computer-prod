from django.shortcuts import render
from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.db.models import Q
from functools import reduce
from datetime import date
from django.db.models import Count

from .models import Quote, Producto
# Create your views here.


class ListaProductos(ListView):
    model = Producto
    paginate_by = 100
    ordering = "-marca"
    template_name = "buscador.html"

    def get_queryset(self):
        result_delete = Producto.objects.filter(fecha__lt=date.today()).delete()
        # print(result_delete)
        return Producto.objects.order_by('-marca', '-precio_dolares')
    
    def get_context_data(self, **kwargs):
        context = super(ListaProductos, self).get_context_data(**kwargs)

        context["prodXproveedor"] = get_num_prod_by_proveedor()

        return context

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
        return Producto.objects.filter(str_query).order_by('-marca', '-precio_dolares')
    

    def get_context_data(self, **kwargs):
        context = super(BuscarProductos, self).get_context_data(**kwargs)

        context["prodXproveedor"] = get_num_prod_by_proveedor()

        return context
    

def get_num_prod_by_proveedor():
    # SELECT proveedor, COUNT(*) FROM Producto GROUP BY proveedor;
    # <QuerySet [{'proveedor': 'memorykings', 'num_prod': 521}, {'proveedor': 'itstore', 'num_prod': 199}, {'proveedor': 'infotec', 'num_prod': 484}]>
    prod_x_proveedor = Producto.objects.filter(fecha=date.today()).values('proveedor').annotate(num_prod=Count('titulo')).order_by('-proveedor')
    return prod_x_proveedor
