# Generated by Django 2.1 on 2018-09-04 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hortadb', '0020_auto_20180904_1413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seed_packet',
            old_name='plant_variety',
            new_name='seed_packet',
        ),
    ]
