# Generated by Django 2.1 on 2018-09-03 12:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hortadb', '0011_auto_20180903_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seed',
            name='date_sow_ini',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='month sowing season starts'),
        ),
    ]
