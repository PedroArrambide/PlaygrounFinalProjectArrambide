from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from .models import Certificado, Colaborador, User
from .forms import ColaboradorForm, CertificadoForm, UserCreationFormCustom, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit  import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin



def index(request):
    return render(request,'index.html')

def inicio(request):
    return render(request, 'inicio.html')

#Colaboradores 

@login_required
def colaboradores(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'colaborador.html',{'colaboradores':colaboradores})



@login_required
def Crear_colaborador(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, request.FILES)
        if form.is_valid():
            colaborador = form.save(commit=False)  
            if 'imagen' in request.FILES:
                colaborador.imagen = request.FILES['imagen']  
            colaborador.save()  
            return redirect('AppCoder:colaboradores')
    else:
        form = ColaboradorForm()
    return render(request, 'colaborador_form.html', {'form': form})

@login_required
def eliminnar_colaborador(request,colaborador_nombre):
    colaborador = Colaborador.objects.get(nombre=colaborador_nombre)
    colaborador.delete()

    colaboradores = Colaborador.objects.all()
    return render(request, 'colaborador.html',{'colaboradores':colaboradores})
@login_required
def editar_colaborador(request,colaborador_nombre):
    colaborador = Colaborador.objects.get(nombre=colaborador_nombre)
    if request.method == 'POST':
        miFormulario = ColaboradorForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            colaborador.nombre = informacion['nombre']
            colaborador.apellido = informacion['apellido']
            colaborador.email = informacion['email']
            colaborador.Cargo = informacion['Cargo']
            colaborador.save()
            return redirect('AppCoder:colaboradores')
    else:
        miFormulario = ColaboradorForm(initial={'nombre':colaborador.nombre,'apellido':colaborador.apellido,
                                             'email': colaborador.email, 'Cargo': colaborador.Cargo})
    return render(request, "editarColaborador.html",{"miFormulario":miFormulario, "colaborador_nombre": colaborador_nombre})

# CERTIFICADO

from django.contrib.auth.decorators import login_required

@login_required
def crear_certificado(request):
    if request.method == 'POST':
        form = CertificadoForm(request.POST, request.FILES)
        if form.is_valid():
            certificado = form.save(commit=False)
            if 'imagen' in request.FILES:
                certificado.imagen = request.FILES['imagen']
            certificado.usuario = request.user
            certificado.save()
            return redirect('AppCoder:certificados')
    else:
        form = CertificadoForm()
    return render(request, 'certificado_form.html', {'form': form})



@login_required
def certificados(request):
    certificado = Certificado.objects.all()
    return render(request, 'certificados.html',{'certificados':certificado})
@login_required
def eliminnar_certificado(request,certificado_nombre):
    certificado = Certificado.objects.get(nombre=certificado_nombre)
    certificado.delete()

    certificado = Certificado.objects.all()
    return render(request, 'certificados.html',{'certificados':certificados})
@login_required
def editar_certificado(request,certificado_nombre):
    certificado= Certificado.objects.get(nombre=certificado_nombre)
    if request.method == 'POST':
        miFormulario = CertificadoForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            certificado.nombre = informacion['nombre']
            certificado.fecha_entrega = informacion['fecha_entrega']
            certificado.entregado = informacion['entregado']
            
            certificado.save()
            return render(request,"inicio.html")
    else:
        miFormulario = CertificadoForm(initial={'nombre':certificado.nombre,'Fecha Entrega':certificado.fecha_entrega})
    return render(request, "editarcertificado.html",{"miFormulario":miFormulario, "certificado_nombre": certificado_nombre})
  
  # LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - LOGIN - 

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm( request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            login(request, user)
            return render(request, "inicio.html", {"mensaje": f'Bienvenido {user.username}'})
    else:
        form = AuthenticationForm()
    return render(request, "login.html",{"form": form})

def registro(request):
    if request.method == 'POST':
        form = UserCreationFormCustom(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()  
            return render(request, 'inicio.html', {"mensaje": "Usuario Creado"})
    else:
        form = UserCreationFormCustom()
    return render(request, "registro.html", {"form": form})

def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=request.user)

        if miFormulario.is_valid():
                if miFormulario.cleaned_data.get('imagen'):
                    usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.avatar.save()

                miFormulario.save()

                return render(request, "registro.html")
    else:
        miFormulario = UserEditForm(initial={'imagen': usuario.avatar.imagen}, instance=request.user)
        return render(request, "editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

    
class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'cambiar_contrasenia.html'
    success_url = reverse_lazy('EditarPerfil')

