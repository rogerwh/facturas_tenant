from django.contrib import admin
from .models import FormaPago

@admin.register(FormaPago)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'created')