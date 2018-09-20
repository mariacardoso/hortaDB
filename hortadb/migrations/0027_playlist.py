# Generated by Django 2.1.1 on 2018-09-20 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hortadb', '0026_species_subspecies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('link', models.URLField()),
            ],
        ),
    ]