from django.contrib import admin
from .models import *
from simplemes.publicadmin import MesObjAdmin


# Register your models here.
class MaterialAttrInline(admin.TabularInline):
    model = MaterialAttr


class MaterialAdmin(MesObjAdmin):
    model = Material

    inlines = [MaterialAttrInline]


class BomTemplateLineInline(admin.TabularInline):
    model = BomTemplateLine


class BomTemplateAdmin(MesObjAdmin):
    model = BomTemplateLine

    inlines = [BomTemplateLineInline]


admin.site.register(Material, MaterialAdmin)
admin.site.register(Product)
