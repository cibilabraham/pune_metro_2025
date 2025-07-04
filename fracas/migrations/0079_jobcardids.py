# Generated by Django 3.2.25 on 2025-06-16 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fracas', '0078_failuredata_deboarding'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCardIDs',
            fields=[
                ('uid_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.CharField(blank=True, max_length=550, null=True)),
                ('month', models.CharField(blank=True, max_length=550, null=True)),
                ('last_id', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Job Card IDs',
            },
        ),
    ]
