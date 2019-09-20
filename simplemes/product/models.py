from django.db import models
from simplemes.publicmodels import CommonField, RowTracking, VolumeField
from simplemes.enums import MAINTENANCE_STATUS


# Create your models here.
class MaterialCategory(CommonField, RowTracking):
    class Meta:
        db_table = 'material_category'
        verbose_name_plural = "Material category"


class MaterialCategoryAttr(RowTracking):
    MATERIAL_CATEGORY_ATTRIBUTES = [
        ('PLANT_CODE', 'Plant code(2 digits)'),
        ('NATION', 'Nation'),
        ('MANAGER', 'Manager''s Name'),
        ('PHONE_NUMBER', 'Contact Phone Number'),
    ]

    material_category = models.ForeignKey(
        'MaterialCategory',
        on_delete=models.CASCADE    # ,
        # db_constraint=False
    )
    attr_name = models.CharField(
        max_length=100,
        choices=MATERIAL_CATEGORY_ATTRIBUTES,
    )
    attr_value = models.CharField(
        max_length=100
    )

    class Meta:
        db_table = 'material_category_attr'
        verbose_name_plural = "Extended attributes"
        constraints = [
            models.UniqueConstraint(fields=['material_category', 'attr_name'], name='uniq_material_category_attr')
        ]


# Create your models here.
class Material(CommonField, RowTracking, VolumeField):
    MATERIAL_UNIT = [
        (1, 'pcs'),
        (10, 'm'),
        (11, 'cm'),
        (12, 'mm'),
        (20, 'g'),
        (21, 'mg'),
        (22, 'kg'),
        (30, 'l'),
        (40, 'cubic meter'),
    ]
    MATERIAL_TYPE = [
        ('NORMAL', 'Normal'),
        ('PRODUCT', 'Product'),
        ('FIXTURE', 'Fixture'),
    ]

    unit = models.SmallIntegerField(
        choices=MATERIAL_UNIT,
        default=1,
        help_text='Unit of consumption'
    )
    material_type = models.CharField(
        max_length=20,
        choices=MATERIAL_TYPE,
        default='NORMAL',
        help_text='Type of the material, product and normal is different',
    )
    price = models.DecimalField(
        default=0,
        decimal_places=9,
        max_digits=50,
        help_text='Price per unit',
    )
    currency = models.CharField(
        max_length=3,
        default='TBD',
        help_text='Currency code of the price',
    )
    revision = models.CharField(
        max_length=20,
        default='0',
        help_text='Revision number',
    )
    status = models.SmallIntegerField(
        choices=MAINTENANCE_STATUS,
        default=100,
        help_text='Status',
    )

    class Meta:
        db_table = 'material'
        verbose_name_plural = "Material master"


class MaterialAttr(RowTracking):
    MATERIAL_ATTRIBUTES = [
        ('PLANT_CODE', 'Plant code(2 digits)'),
        ('NATION', 'Nation'),
        ('MANAGER', 'Manager''s Name'),
        ('PHONE_NUMBER', 'Contact Phone Number'),
    ]

    material = models.ForeignKey(
        'Material',
        on_delete=models.CASCADE    # ,
        # db_constraint=False
    )
    attr_name = models.CharField(
        max_length=100,
        choices=MATERIAL_ATTRIBUTES,
    )
    attr_value = models.CharField(
        max_length=100
    )

    class Meta:
        db_table = 'material_attr'
        verbose_name_plural = "Extended attributes"
        constraints = [
            models.UniqueConstraint(fields=['material', 'attr_name'], name='uniq_material_attr')
        ]
