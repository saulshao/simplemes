from django.db import models
from simplemes.publicmodels import CommonField, RowTracking


# Create your models here.
class FactoryCommon(CommonField, RowTracking):
    location = models.TextField(
        max_length=100,
        default='TBD',
        help_text='Position of the location, e.g. coordinates'
    )

    class Meta:
        abstract = True


class Factory(FactoryCommon):
    class Meta:
        db_table = 'factory'
        verbose_name_plural = "Factories"


class FactoryAttr(RowTracking):
    FACTORY_ATTRIBUTES = [
        ('PLANT_CODE', 'Plant code(2 digits)'),
        ('NATION', 'Nation'),
        ('MANAGER', 'Manager''s Name'),
        ('PHONE_NUMBER', 'Contact Phone Number'),
    ]

    factory = models.ForeignKey(
        Factory,
        on_delete=models.CASCADE,
        related_name='attributes'    # ,
        # db_constraint=False
    )
    attr_name = models.CharField(
        max_length=100,
        choices=FACTORY_ATTRIBUTES,
    )
    attr_value = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.attr_name

    class Meta:
        db_table = 'factory_attr'
        verbose_name_plural = "Extended attributes"
        constraints = [
            models.UniqueConstraint(fields=['factory', 'attr_name'], name='uniq_factory_attr')
        ]


class Workshop(FactoryCommon):
    factory = models.ForeignKey(
        Factory,
        on_delete=models.PROTECT,
        related_name='workshops'
        # db_constraint=False
    )

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'workshop'


class WorkshopAttr(RowTracking):
    WORKSHOP_ATTRIBUTES = [
        ('MANAGER', 'Manager''s Name'),
        ('PHONE_NUMBER', 'Contact Phone Number'),
    ]

    workshop = models.ForeignKey(
        Workshop,
        on_delete=models.CASCADE,
        related_name='attributes',    # ,
        # db_constraint=False
    )
    attr_name = models.CharField(
        max_length=100,
        choices=WORKSHOP_ATTRIBUTES
    )
    attr_value = models.CharField(
        max_length=100
    )

    class Meta:
        db_table = 'workshop_attr'
        verbose_name_plural = "Extended attributes"
        constraints = [
            models.UniqueConstraint(fields=['workshop', 'attr_name'], name='uniq_workshop_attr')
        ]


class Line(FactoryCommon):
    workshop = models.ForeignKey(
        Workshop,
        on_delete=models.PROTECT,
        related_name='lines',
        # db_constraint=False
    )

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'line'


class LineAttr(RowTracking):
    LINE_ATTRIBUTES = [
        ('LEADER', 'Leader''s Name'),
        ('PHONE_NUMBER', 'Contact Phone Number'),
    ]

    line = models.ForeignKey(
        Line,
        on_delete=models.CASCADE,
        related_name='attributes',
        # db_constraint=False
    )
    attr_name = models.CharField(
        max_length=100,
        choices=LINE_ATTRIBUTES
    )
    attr_value = models.CharField(
        max_length=100
    )

    class Meta:
        db_table = 'line_attr'
        verbose_name_plural = "Extended attributes"
        constraints = [
            models.UniqueConstraint(fields=['line', 'attr_name'], name='uniq_line_attr')
        ]


class Station(FactoryCommon):
    line = models.ForeignKey(
        Line,
        on_delete=models.PROTECT,
        related_name='stations',
        # db_constraint=False
    )

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'station'


class StationAttr(RowTracking):
    STATION_ATTRIBUTES = [
        ('DANGEROUS', 'Dangrous(Y/N)'),
        ('AUTOMATE', 'Automate(Y/N)'),
        ('ROBOT', 'Robot(Y/N)'),
    ]

    station = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        related_name='attributes',
        # db_constraint=False
    )
    attr_name = models.CharField(
        max_length=100,
        choices=STATION_ATTRIBUTES
    )
    attr_value = models.CharField(
        max_length=100
    )

    class Meta:
        db_table = 'station_attr'
        verbose_name_plural = "Extended attributes"
        constraints = [
            models.UniqueConstraint(fields=['station', 'attr_name'], name='uniq_station_attr')
        ]
