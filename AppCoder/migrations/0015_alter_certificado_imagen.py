# Generated by Django 4.2.4 on 2023-09-10 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0014_certificado_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificado',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='certificados_imagenes/'),
        ),
    ]
