from django.db import models
from tenant_schemas.models import TenantMixin

class Empresa(TenantMixin):

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última Actualización')

    nombre = models.CharField(max_length=80, unique=True)
    direccion = models.TextField(max_length=100, blank=True)

    is_active = models.BooleanField(default=True)
    auto_create_schema = True
    # pais = CountryField(default='MX')

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return f'{self.nombre}'

    @staticmethod
    def generar_empresas_random():
        lista_empresas = [
            "nupython", "comuppython", "com101python", "cominstapython", "comrepython", "comourpython", "combuypython", 
            "comhdpython", "commaxpython", "comnextpython", "compythonyou", "compythonnew", "compythonsumo", "compythonmob", 
            "compythonjar", "compythonegg", "compython24x7", "compythonzoom", "compythonbros", "compythonsale", "comecopython", 
            "compythonsearch", "comtravelpython", "commobilepython", "cominfopython", "compythonmobile", "comvideopython", 
            "compythonmap", "comapppython", "comcitypython", "comlocalpython", "comstarpython", "comdesignpython", 
            "comblogpython"]

        # lista_empresas = [
        #     "Python Global","Craft Python","Python Cup","NewAge Python","Python Network","Plan Python","Electro Python","Unity Python","Python Solar","Python Preview","Python Sells","Patrol Python",
        #     "Stallion Python","Morning Python","Conservative Python","Fluid Python","FreshStart Python","Operation Python","Python Workshop","Python Sky",
        #     "Python Look","BlueFire Python","Breeze Python","Handy Python",
        #     "Python Wizard","Chrome Python","Altitude Python","Python Reference","Safeguard Python","Crossover Python","Pentagon Python","Python Precision","Python Logistics","Acuity Python","Python Standard","Power Python",
        #     "Management Python","Python Complete"
        # ]

        for nombre in lista_empresas:
            empresa = Empresa()
            empresa.nombre = nombre
            empresa.domain_url = f'{nombre}.localhost'
            empresa.schema_name = nombre
            empresa.direccion = "Av. Caracola. Interseccion Concha y Coral"
            empresa.save()
            print(f'{empresa.nombre}')