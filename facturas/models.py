from django.db import models
from empresa.models import Empresa
from pasarelas.models import FormaPago

# Create your models here.
class Factura(models.Model):
    pendiente = "Pendiente de Pago"
    pagada = "Pagada"
    revision = "En Revisión"
    transferida = "Transferida"
    cancelada = "Cancelada"

    ESTADO_LIST = [pendiente, pagada, revision, transferida, cancelada]

    ESTADO = (
        (pendiente, pendiente),
        (pagada, pagada),
        (revision, revision),
        (transferida, transferida),
        (cancelada, cancelada)
    )
    s = models.DecimalField(max_digits=10, decimal_places=2, default=100)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    impuestos = models.DecimalField(max_digits=15, decimal_places=2, default=16, help_text="Porcentaje: Ej. 16%")
    total_impuestos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=25, choices=ESTADO, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última Actualización')

    forma_pago = models.ForeignKey('pasarelas.FormaPago', related_name="formapago_facturas", null=True,
                                   on_delete=models.SET_NULL)
    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"

    def __str__(self):
        return f'{self.id}'

    @staticmethod
    def crear_facturas_random(schema):
        import random
        from tenant_schemas.utils import schema_context

        with schema_context(schema):
            formas_pago = FormaPago.objects.all()
            
            for x in range(random.randrange(800, 1000)):

                subtotal = random.randrange(500, 1001)
                total_impuestos = subtotal * 0.16
                total = subtotal + total_impuestos
                estado = random.choice(Factura.ESTADO_LIST)
                forma_pago = random.choice(formas_pago)

                factura = Factura()
                factura.sub_total = subtotal
                factura.total_impuestos = total_impuestos
                factura.total = total
                factura.estado = estado
                factura.forma_pago = forma_pago

                factura.save()
            