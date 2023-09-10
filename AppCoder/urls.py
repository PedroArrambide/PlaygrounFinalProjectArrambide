from django.urls import path

from AppCoder import views

from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
   
    path('', views.inicio, name="inicio"), 
    
    path('colaboradores', views.colaboradores, name="colaboradores"),
    path('colaborador/create/', views.Crear_colaborador, name="colaborador-create"),
    path('eliminarColaborador/<str:colaborador_nombre>/', views.eliminnar_colaborador, name="eliminar-colaborador"),
    path('editarColaborador/<str:colaborador_nombre>/', views.editar_colaborador, name="editar-colaborador"),
    
    path('certificados', views.certificados, name="certificados"),
    path('certificado/create/', views.crear_certificado, name="certificado-create"),
    path('eliminarCertificado/<str:certificado_nombre>/', views.eliminnar_certificado, name="eliminar-certificado"),
    path('editarCertificado/<str:certificado_nombre>/', views.editar_certificado, name="editar-certificado"),
    
    path('login/', views.login_request, name="login"),
    path('registro/', views.registro, name="registro"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('editarPerfil/', views.editarPerfil, name="EditarPerfil"),
    path('cambiarContrasenia/',views.CambiarContrasenia.as_view() , name="CambiarContrasenia"),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

