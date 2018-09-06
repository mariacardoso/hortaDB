# Generated by Django 2.1 on 2018-08-27 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variety', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=50)),
                ('date_sown', models.DateTimeField(verbose_name='date sown')),
                ('date_trans', models.DateTimeField(verbose_name='date transplant')),
                ('date_trans_pred', models.DateTimeField(verbose_name='date predicted transplant')),
            ],
        ),
        migrations.CreateModel(
            name='Plant_Generic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_name', models.CharField(max_length=100)),
                ('family', models.CharField(max_length=100)),
                ('genus', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='plant',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hortadb.Plant_Generic'),
        ),
    ]
