# Generated by Django 2.1 on 2018-09-09 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hortadb', '0023_auto_20180906_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='seed',
            name='days_to_maturity',
            field=models.IntegerField(blank=True, null=True, verbose_name='days to maturity'),
        ),
        migrations.AddField(
            model_name='seed',
            name='fruit_size',
            field=models.FloatField(blank=True, null=True, verbose_name='average size of fruit [cm]'),
        ),
        migrations.AddField(
            model_name='seed',
            name='fruit_weight',
            field=models.FloatField(blank=True, null=True, verbose_name='average weight of fruit [cm]'),
        ),
        migrations.AddField(
            model_name='seed',
            name='plant_spacing',
            field=models.FloatField(blank=True, null=True, verbose_name='average space between plants [cm]'),
        ),
        migrations.AddField(
            model_name='seed',
            name='row_spacing',
            field=models.FloatField(blank=True, null=True, verbose_name='average space between rows [cm]'),
        ),
    ]
