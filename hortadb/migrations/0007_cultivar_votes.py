# Generated by Django 2.1 on 2018-09-01 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('hortadb', '0006_delete_plant'),
    ]

    operations = [
        migrations.AddField(
            model_name='cultivar',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]