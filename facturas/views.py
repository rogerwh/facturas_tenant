from django.shortcuts import render
from .models import Factura
from empresa.models import Empresa
from django.contrib import messages
import random

def factura_empresa(request):
    messages.success(request, "Probando Mensajes {0}".format(random.randint(10, 100)))
    empresa = request.tenant.schema_name
    facturas_empresa = Factura.objects.select_related("forma_pago").all()
    total_facturas = facturas_empresa.count()
    return render(request, 'facturas_empresa.html', {
        "facturas": facturas_empresa, "empresa":empresa, "total_facturas": total_facturas})