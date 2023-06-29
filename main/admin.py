from django.contrib import admin

from main.models import Quote, Producto

# Register your models here.


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('author', 'text','fecha' )

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'precio_soles','precio_dolares', 'categoria', 'marca', 'proveedor', 'fecha' )


admin.site.register(Quote, QuoteAdmin)
admin.site.register(Producto, ProductoAdmin)