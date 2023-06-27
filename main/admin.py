from django.contrib import admin

from main.models import Quote

# Register your models here.
from main.models import Quote

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('author', 'text','fecha' )


admin.site.register(Quote, QuoteAdmin)