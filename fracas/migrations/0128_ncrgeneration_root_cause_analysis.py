# Generated by Django 3.2.25 on 2025-07-17 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fracas', '0127_ncrimageslist'),
    ]

    operations = [
        migrations.AddField(
            model_name='ncrgeneration',
            name='root_cause_analysis',
            field=models.CharField(default=0, max_length=550),
        ),
    ]
