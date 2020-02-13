from django.db import models

class FormaPago(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=100, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última Actualización')

    class Meta:
        verbose_name = "Forma de Pago"
        verbose_name_plural = "Formas de Pago"

    def __str__(self):
        return f'{self.nombre}'