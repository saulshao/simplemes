# Generated by Django 2.2.5 on 2019-09-14 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mesfactory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='factory',
            table='factory',
        ),
        migrations.AlterModelTable(
            name='line',
            table='line',
        ),
        migrations.AlterModelTable(
            name='station',
            table='Station',
        ),
        migrations.AlterModelTable(
            name='workshop',
            table='workshop',
        ),
    ]
