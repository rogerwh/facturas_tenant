from django.shortcuts import render
from .models import Factura
from empresa.models import Empresa

def factura_empresa(request):
    empresa = request.tenant.schema_name
    print(request.tenant.schema_name)
    facturas_empresa = Factura.objects.select_related("forma_pago").all()
    total_facturas = facturas_empresa.count()
    return render(request, 'facturas_empresa.html', {
        "facturas": facturas_empresa, "empresa":empresa, "total_facturas": total_facturas})