from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', factura_empresa, name="factura_empresa"),
]