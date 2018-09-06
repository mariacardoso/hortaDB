# Generated by Django 2.1 on 2018-08-27 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hortadb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variety', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=50)),
                ('date_sow_ini', models.DateTimeField(verbose_name='date sowing season starts')),
                ('date_sow_end', models.DateTimeField(verbose_name='date sowing season ends')),
                ('date_packing', models.DateTimeField(verbose_name='date packing of seeds')),
                ('date_validity', models.DateTimeField(verbose_name='expir date of seeds')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hortadb.Plant_Generic')),
            ],
        ),
        migrations.RemoveField(
            model_name='plant',
            name='plant',
        ),
        migrations.DeleteModel(
            name='Plant',
        ),
    ]
