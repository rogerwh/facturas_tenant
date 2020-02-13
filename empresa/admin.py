from django.contrib import admin
from .models import Empresa

@admin.register(Empresa)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'created_at')