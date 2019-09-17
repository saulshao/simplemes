from django.contrib import admin
from simplemes.publicadmin import MesObjAdmin
from .models import Factory, Workshop, Line, Station
# Register your models here.


class WorkshopInline(admin.TabularInline):
    model = Workshop


class FactoryAdmin(MesObjAdmin):
    inlines = [WorkshopInline]


class LineInline(admin.TabularInline):
    model = Line


class WorkshopAdmin(MesObjAdmin):
    inlines = [LineInline]


class StationInline(admin.TabularInline):
    model = Station


class LineAdmin(MesObjAdmin):
    inlines = [StationInline]


class StationAdmin(MesObjAdmin):
    pass

admin.site.register(Factory, FactoryAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Line, LineAdmin)
admin.site.register(Station, StationAdmin)
