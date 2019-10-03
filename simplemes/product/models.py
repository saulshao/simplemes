from django.db import models
from simplemes.publicmodels import CommonField, RowTracking, VolumeField
from simplemes.enums import MAINTENANCE_STATUS


# Create your models here.
class MaterialCategory(CommonField, RowTracking):

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'material_category'
        verbose_name_plural = "Material category"


class MaterialCategoryAttr(RowTracking):
    MATERIAL_CATEGORY_ATTRIBUTES = [
        ('SN_PREFIX', 'Serial Number Prefix'),
        ('Attr2', 'Attr2'),
        ('Attr3', 'Attr3'),
        ('Attr4', 'Attr4'),
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

    def __str__(self):
        return self.attr_name

    class Meta:
        db_table = 'material_category_attr'
        verbose_name_plural = 'Extended attributes'
        constraints = [
            models.UniqueConstraint(fields=['material_category', 'attr_name'], name='uniq_material_category_attr')
        ]


class BomTemplate(CommonField, RowTracking):
    revision = models.CharField(
        max_length=20,
        default='0',
        help_text='Revision number of the BOM',
    )
    status = models.SmallIntegerField(
        choices=MAINTENANCE_STATUS,
        default=100,
        help_text='Status,very important for maintenance',
    )

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'bom_template'
        verbose_name_plural = 'BOM template'


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
        ('EQUIPMENT', 'Equipment'),
    ]

    material_category = models.ForeignKey(
        MaterialCategory,
        on_delete=models.PROTECT,
        default=1,
        help_text='Link to material category',
    )
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
    bom_template = models.ForeignKey(
        BomTemplate,
        on_delete=models.PROTECT,
        default=-1,
        db_constraint=False,
        help_text='Link to BOM template',
    )

    def __str__(self):
        return "%s-%s" % (self.code, self.name)

    class Meta:
        db_table = 'material'
        verbose_name_plural = "Materials"


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

    def __str__(self):
        return self.attr_name

    class Meta:
        db_table = 'material_attr'
        verbose_name_plural = 'Extended attributes'
        constraints = [
            models.UniqueConstraint(fields=['material', 'attr_name'], name='uniq_material_attr')
        ]


class Product(RowTracking):
    material = models.OneToOneField(
        Material,
        on_delete=models.PROTECT,
        primary_key=True,
        # db_constraint=False
    )

    def __str__(self):
        return self.material.code

    class Meta:
        db_table = 'product'
        verbose_name_plural = 'Products'

'''
class ProductBOM(RowTracking):
    product = models.ForeignKey(
        'Product',
        on_delete=models.PROTECT,
    )
    revision = models.CharField(
        max_length=20,
        default='0',
        help_text='Revision number',
    )
    status = models.SmallIntegerField(
        choices=MAINTENANCE_STATUS,
        default=100,
        help_text='Status,very important for maintenance',
    )

    def __str__(self):
        return "BOM of %s" % self.product.material.code

    class Meta:
        db_table = 'product_bom'
        verbose_name_plural = 'product BOM'
'''


class BomTemplateLine(RowTracking):
    bom_template = models.ForeignKey(
        'BomTemplate',
        on_delete=models.CASCADE,
        help_text='Please select existed bom template',
    )
    material = models.ForeignKey(
        'Material',
        on_delete=models.CASCADE,
        help_text='Please select existed material',
    )
    quantity = models.DecimalField(
        max_digits=20,
        decimal_places=6,
        default=1,
    )

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'bom_template_line'
        verbose_name_plural = 'BOM template line'
        constraints = [
            models.UniqueConstraint(fields=['bom_template', 'material'], name='uniq_bom_template_line')
        ]
