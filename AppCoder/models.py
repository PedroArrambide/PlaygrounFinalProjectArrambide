from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone

class Colaborador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    Cargo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='colaborador_imagenes/',null=True,blank=True)
    def __str__(self):
        return  f" Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - cargo: {self.Cargo}"


class Certificado(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_entrega = models.DateField()
    imagen = models.ImageField(upload_to='certificados_imagenes/', null=True, blank=True)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f" Nombre: {self.nombre} - Fecha Entrega: {self.fecha_entrega}"
    

class Avatar(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"



