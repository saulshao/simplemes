from django.contrib import admin
from simplemes.publicadmin import MesObjAdmin
from .models import Factory, Workshop, Line, Station, Location
from .models import FactoryAttr, WorkshopAttr, LineAttr, StationAttr
# Register your models here.


class LocationInline(admin.TabularInline):
    model = Location

class LocationAdmin(MesObjAdmin):
    pass


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
    # list_display = MesObjAdmin.list_display.insert(2, 'get_factory_code')
    # list_display_links = ('get_factory_code', )
    inlines = [WorkshopAttrInline, LineInline]

    # def get_factory_code(self, obj):
    #   return self.factory
    # get_factory_code.admin_order_field = 'factory'
    # get_factory_code.short_description = 'Factory'


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
    
admin.site.register(Location, LocationAdmin)

admin.site.register(Factory, FactoryAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Line, LineAdmin)
admin.site.register(Station, StationAdmin)

admin.site.site_header = "Experimental MES Admin"
admin.site.site_title = "Experimental MES Admin Portal"
admin.site.index_title = "Welcome to experimental MES Portal"
