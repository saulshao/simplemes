# Generated by Django 2.2.5 on 2019-09-16 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mesfactory', '0005_auto_20190915_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factory',
            name='description',
            field=models.TextField(max_length=512),
        ),
        migrations.AlterField(
            model_name='line',
            name='description',
            field=models.TextField(max_length=512),
        ),
        migrations.AlterField(
            model_name='station',
            name='description',
            field=models.TextField(max_length=512),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='description',
            field=models.TextField(max_length=512),
        ),
    ]