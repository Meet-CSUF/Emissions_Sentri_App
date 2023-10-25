from django.contrib import admin
from .models import Emission

# Register your models here.
class EmissionsAdmin(admin.ModelAdmin):
    list_display = ("id", "Date_Created", "Accounting_Period", "Scope1", "Scope2", "Scope3")
    list_filter = ("Accounting_Period", "Date_Created")

admin.site.register(Emission, EmissionsAdmin)