# Generated by Django 4.2.4 on 2023-09-10 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0007_colaborador_delete_profesor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
    ]