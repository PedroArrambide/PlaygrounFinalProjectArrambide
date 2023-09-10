# Generated by Django 4.2.4 on 2023-09-10 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0012_remove_certificado_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificado',
            name='colaborador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AppCoder.colaborador'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='certificado',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='colaborador_imagenes/'),
        ),
        migrations.AlterField(
            model_name='certificado',
            name='descripcion',
            field=models.TextField(),
        ),
    ]
