# Generated by Django 4.2.4 on 2023-08-25 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_rename_mombre_entregable_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='apellido',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='apellido',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='profesion',
            field=models.CharField(max_length=100),
        ),
    ]
