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
    model = BomTemplate

    inlines = [BomTemplateLineInline]


class MaterialCategoryInline(admin.TabularInline):
    model = MaterialCategoryAttr


class MaterialCategoryAdmin(MesObjAdmin):
    model = MaterialCategory

    inlines = [MaterialCategoryInline]


admin.site.register(MaterialCategory, MaterialCategoryAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(BomTemplate, BomTemplateAdmin)
admin.site.register(Product)
