from django.contrib import admin
from simplemes.publicmodels import RowTracking


class MesObjAdmin(admin.ModelAdmin):
    '''
        Admin view for most entity model
    '''
    # Default columns in query result list
    list_display = [
        'code',
        'name',
        'description',
        'created_by',
        'created_on',
        'updated_by',
        'updated_on'
    ]

    # assign values for update record automatically according the current user
    def save_model(self, request, obj, form, change):
        if request.user.is_authenticated:
            if not obj.pk:
                obj.created_by = request.user.username
            obj.updated_by = request.user.username
        else:
            if not obj.pk:
                obj.created_by = 'INIT'
                obj.updated_by = obj.created_by
        super().save_model(request, obj, form, change)

    # assign values for update record automatically according the current user
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)

        for instance in instances:
            # Check if it is the correct type of inline
            if isinstance(instance, RowTracking):
                if not instance.pk:
                    instance.created_by = request.user.username
                instance.updated_by = request.user.username
                instance.save()
