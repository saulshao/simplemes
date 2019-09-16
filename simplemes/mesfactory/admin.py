from django.contrib import admin
from simplemes.publicadmin import MesObjAdmin
from .models import Factory, Workshop, Line, Station
# Register your models here.


class WorkshopInline(admin.TabularInline):
    model = Workshop


class FactoryAdmin(MesObjAdmin):
    inlines = [WorkshopInline]

admin.site.register(Factory, FactoryAdmin)
