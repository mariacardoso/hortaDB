# Generated by Django 2.1 on 2018-09-03 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hortadb', '0014_auto_20180903_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='species',
            name='pub_date',
        ),
    ]
