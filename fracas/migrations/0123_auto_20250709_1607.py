# Generated by Django 3.2.25 on 2025-07-09 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fracas', '0122_auto_20250709_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='ncrgeneration',
            name='fnl_designation',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='ncrgeneration',
            name='fnl_name',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='ncrgeneration',
            name='no_of_day_open',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='ncrgeneration',
            name='physical_closure',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='ncrgeneration',
            name='physical_closure_rca_capa',
            field=models.TextField(blank=True),
        ),
    ]
