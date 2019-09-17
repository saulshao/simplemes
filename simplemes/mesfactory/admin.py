from django.contrib import admin
from simplemes.publicadmin import MesObjAdmin
from .models import Factory, Workshop, Line, Station
from .models import FactoryAttr, WorkshopAttr, LineAttr, StationAttr
# Register your models here.


class WorkshopInline(admin.TabularInline):
    model = Workshop


class FactoryAttrInline(admin.TabularInline):
    model = FactoryAttr


class FactoryAdmin(MesObjAdmin):
    inlines = [FactoryAttrInline, WorkshopInline]


class LineInline(admin.TabularInline):
    model = Line


class WorkshopAttrInline(admin.TabularInline):
    model = WorkshopAttr


class WorkshopAdmin(MesObjAdmin):
    inlines = [WorkshopAttrInline, LineInline]


class StationInline(admin.TabularInline):
    model = Station


class LineAttrInline(admin.TabularInline):
    model = LineAttr


class LineAdmin(MesObjAdmin):
    inlines = [LineAttrInline, StationInline]


class StationAttrInline(admin.TabularInline):
    model = StationAttr


class StationAdmin(MesObjAdmin):
    inlines = [StationAttrInline]

admin.site.register(Factory, FactoryAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Line, LineAdmin)
admin.site.register(Station, StationAdmin)
