from django.contrib import admin


class MesObjAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name',
        'description',
        'created_by',
        'created_on',
        'updated_by',
        'updated_on'
        )

    def save_model(self, request, obj, form, change):
        if request.user.is_authenticated:
            if not obj.pk:
                obj.created_by = request.user.username
            obj.updated_by = request.user.username
        else:
            obj.created_by = 'INIT'
            obj.updated_by = obj.created_by
        super().save_model(request, obj, form, change)
