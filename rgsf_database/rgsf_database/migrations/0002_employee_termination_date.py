# Generated by Django 2.1.2 on 2020-12-12 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rgsf_database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='termination_date',
            field=models.TextField(default='', max_length=200),
        ),
    ]
