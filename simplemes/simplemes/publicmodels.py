from django.db import models


class CommonField(models.Model):
    '''
        All tables which indicate primary objects need these columns
    '''
    code = models.CharField(
        max_length=50,
        default='None',
        unique=True,
        blank=False,
        help_text='Unique code, only specified characters are allowed')
    name = models.CharField(
        max_length=50,
        default='None',
        blank=False,
        help_text='Name, most characters are allowed')
    description = models.CharField(max_length=512)

    class Meta:
        abstract = True


class RowTracking(models.Model):
    '''
        All tables need these columns
    '''
    created_by = models.CharField(
        max_length=50,
        default='INIT',
        editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(
        max_length=50,
        default='INIT',
        editable=False)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
