from django import forms
from .models import  Certificado, Colaborador, User
from django.contrib.auth.forms import  UserCreationForm, UserChangeForm

class CertificadoForm(forms.ModelForm):
    class Meta:
        model= Certificado
        fields = '__all__'

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model= Colaborador
        fields = '__all__'

class UserCreationFormCustom(UserCreationForm):
    username = forms.CharField(label='Usuario')
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label= "Nombre")
    last_name = forms.CharField(label= "Apellido")
    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):

    password=None
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    imagen = forms.ImageField(label="Avatar", required=False)

    class Meta:
        model = User
        fields = ['email','last_name','first_name','imagen']

