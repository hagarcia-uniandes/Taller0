"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django import contrib
from django.urls import path
from apps.eventos.views import EventosListado, EventoDetalle, EventoCrear, EventoActualizar, EventoEliminar, RegistroUsuario
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from apps.eventos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'home/', LoginView.as_view(template_name = 'index.html'), name='login'),
    path('registro/', RegistroUsuario.as_view(template_name = "eventos/registro.html"), name='registro'),
    path('eventos/', EventosListado.as_view(template_name = "eventos/listado.html"), name='leer'),
    path('eventos/detalle/<int:pk>', EventoDetalle.as_view(template_name = "eventos/detalles.html"), name='detalles'),
    path('eventos/crear', EventoCrear.as_view(template_name = "eventos/crear.html"), name='crear'),
    path('eventos/editar/<int:pk>', EventoActualizar.as_view(template_name = "eventos/actualizar.html"), name='actualizar'), 
    path('eventos/eliminar/<int:pk>', EventoEliminar.as_view(), name='eliminar'),    
]
