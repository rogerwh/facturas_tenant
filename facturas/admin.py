from django.contrib import admin
from .models import Factura

@admin.register(Factura)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'total', 'estado')