# Generated by Django 2.2.5 on 2019-09-26 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20190926_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='material_category',
            field=models.ForeignKey(default=1, help_text='Link to material category', on_delete=django.db.models.deletion.PROTECT, to='product.MaterialCategory'),
        ),
        migrations.AlterField(
            model_name='bomtemplate',
            name='status',
            field=models.SmallIntegerField(choices=[(100, 'CREATE'), (200, 'RELEASE'), (300, 'DRAFT'), (400, 'EXPIRED')], default=100, help_text='Status,very important for maintenance'),
        ),
        migrations.AlterField(
            model_name='material',
            name='bom_template',
            field=models.ForeignKey(db_constraint=False, default=-1, help_text='Link to BOM template', on_delete=django.db.models.deletion.PROTECT, to='product.BomTemplate'),
        ),
        migrations.AlterField(
            model_name='material',
            name='height',
            field=models.DecimalField(decimal_places=9, default=0, help_text='Height of the object(mm)', max_digits=30),
        ),
        migrations.AlterField(
            model_name='material',
            name='length',
            field=models.DecimalField(decimal_places=9, default=0, help_text='Length of the object(mm) ', max_digits=30),
        ),
        migrations.AlterField(
            model_name='material',
            name='status',
            field=models.SmallIntegerField(choices=[(100, 'CREATE'), (200, 'RELEASE'), (300, 'DRAFT'), (400, 'EXPIRED')], default=100, help_text='Status'),
        ),
        migrations.AlterField(
            model_name='material',
            name='width',
            field=models.DecimalField(decimal_places=9, default=0, help_text='Width of the object(mm)', max_digits=30),
        ),
        migrations.AlterField(
            model_name='materialcategoryattr',
            name='attr_name',
            field=models.CharField(choices=[('SN_PREFIX', 'Serial Number Prefix'), ('Attr2', 'Attr2'), ('Attr3', 'Attr3'), ('Attr4', 'Attr4')], max_length=100),
        ),
    ]