# Generated by Django 2.1 on 2018-09-03 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hortadb', '0017_auto_20180903_1523'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seed_packet',
            options={'verbose_name': 'seed packet', 'verbose_name_plural': 'seed packets'},
        ),
        migrations.AlterField(
            model_name='seed_packet',
            name='weight',
            field=models.IntegerField(blank=True, null=True, verbose_name='weight of seed bag [g]'),
        ),
    ]
