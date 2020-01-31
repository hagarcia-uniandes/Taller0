from django.shortcuts import render
 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Evento
 
from django.urls import reverse
 
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
 
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.eventos.forms import RegistroForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login

from django.contrib.auth.mixins import LoginRequiredMixin


class RegistroUsuario(SuccessMessageMixin, CreateView):
    model = User
    form_class = RegistroForm
    success_message = 'Usuario Creado Correctamente !' 

    def get_success_url(self):        
        return reverse('login')

class EventosListado(LoginRequiredMixin, ListView): 
    model = Evento
    login_url = '/home/'
    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return Evento.objects.filter(usuario=self.request.user).order_by('-fecha_inicio')
 
class EventoDetalle(LoginRequiredMixin, DetailView): 
    model = Evento
    login_url = '/home/'
    redirect_field_name = 'redirect_to'

class EventoCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    model = Evento
    fields = [
        'nombre',
        'categoria',
        'lugar',
        'direccion',
        'fecha_inicio',
        'fecha_fin',
        'tipo',
    ] 
    success_message = 'Evento Creado Correctamente !' 
    login_url = '/home/'
    redirect_field_name = 'redirect_to'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_success_url(self):        
        return reverse('leer') 
    

class EventoActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = Evento
    form = Evento
    fields = "__all__"  
    success_message = 'Evento Actualizado Correctamente !'
    login_url = '/home/'
    redirect_field_name = 'redirect_to'
 
    def get_success_url(self):               
        return reverse('leer') 

class EventoEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
    model = Evento 
    form = Evento
    fields = "__all__"
    login_url = '/home/'
    redirect_field_name = 'redirect_to'     
 
    def get_success_url(self): 
        success_message = 'Evento Eliminado Correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('leer') 

def login(request):
    if request.method == 'GET': # If the form has been submitted...
        form = LoginView(request.GET) # A form bound to the POST data
        if request.user.is_authenticated(): # All validation rules pass
           return HttpResponseRedirect('eventos/')
