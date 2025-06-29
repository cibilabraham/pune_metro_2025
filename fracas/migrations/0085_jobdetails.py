# Generated by Django 3.2.25 on 2025-06-17 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fracas', '0084_auto_20250617_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobDetails',
            fields=[
                ('job_details_id', models.AutoField(primary_key=True, serialize=False)),
                ('s_no', models.CharField(blank=True, max_length=550, null=True)),
                ('job_description', models.TextField(blank=True, null=True)),
                ('is_active', models.IntegerField(default=0)),
                ('job_card_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fracas.jobcard')),
            ],
            options={
                'verbose_name_plural': 'Job details',
            },
        ),
    ]
