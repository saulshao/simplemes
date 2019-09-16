from django.db import models
from simplemes.publicmodels import CommonField, RowTracking


# Create your models here.
class FactoryCommon(CommonField, RowTracking):
    location = models.TextField(
        max_length=100,
        default='TBD'
    )

    class Meta:
        abstract = True


class Factory(FactoryCommon):
    class Meta:
        db_table = 'factory'


class Workshop(FactoryCommon):
    factory = models.ForeignKey(
        'Factory',
        on_delete=models.PROTECT #,
        #db_constraint=False
    )

    class Meta:
        db_table = 'workshop'


class Line(FactoryCommon):
    workshop = models.ForeignKey(
        'Workshop',
        on_delete=models.PROTECT #,
        #db_constraint=False
    )

    class Meta:
        db_table = 'line'


class Station(FactoryCommon):
    line = models.ForeignKey(
        'Line',
        on_delete=models.PROTECT #,
        #db_constraint=False
    )

    class Meta:
        db_table = 'station'

