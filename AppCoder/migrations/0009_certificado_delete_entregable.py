# Generated by Django 4.2.4 on 2023-09-10 20:47

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0008_delete_curso_delete_estudiante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', ckeditor.fields.RichTextField()),
                ('fecha_entrega', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
    ]