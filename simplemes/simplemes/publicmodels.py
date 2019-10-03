from django.db import models
from django.conf import settings


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
    description = models.TextField(
        max_length=512,
        default='None',
        help_text='Use short sentence to discribe your object')

    def __str__(self):
        return self.code

    class Meta:
        abstract = True


class RowTracking(models.Model):
    '''
        All tables need these columns
    '''
    created_by = models.CharField(
        max_length=50,
        default=settings.AUTH_USER_MODEL,
        editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(
        max_length=50,
        default=settings.AUTH_USER_MODEL,
        editable=False)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class VolumeField(models.Model):
    '''
        Three columns of the volume
    '''
    length = models.DecimalField(
        default=0,
        decimal_places=9,
        max_digits=30,
        help_text='Length of the object(mm) '
    )
    width = models.DecimalField(
        default=0,
        decimal_places=9,
        max_digits=30,
        help_text='Width of the object(mm)'
    )
    height = models.DecimalField(
        default=0,
        decimal_places=9,
        max_digits=30,
        help_text='Height of the object(mm)'
    )

    class Meta:
        abstract = True
