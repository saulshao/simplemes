# Generated by Django 2.2.5 on 2019-09-14 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mesfactory', '0003_auto_20190915_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='factory',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='line',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='station',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='workshop',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='factory',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='line',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]