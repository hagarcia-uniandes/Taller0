from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    nombre = models.CharField(max_length = 200, blank=True, help_text='Nombre del evento')
    CATEGORY = (
        ('c', 'Conferencia'),
        ('s', 'Seminario'),
        ('g', 'Congreso'),
        ('u', 'Curso'),
    )
    categoria = models.CharField(max_length=1, choices=CATEGORY, blank=True, default='c', help_text='Categorìa del evento')
    lugar = models.CharField(max_length = 200, blank=True, help_text='Lugar del evento')
    direccion = models.CharField(max_length = 200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    TYPE = (
        ('p', 'Presencial'),
        ('v', 'Virtual'),
    )
    tipo = models.CharField(max_length=1, choices=TYPE, blank=True, default='c', help_text='Tipo de evento')
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
         db_table = 'evento'