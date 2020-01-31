# Generated by Django 2.2.9 on 2020-01-30 02:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, help_text='Nombre del evento', max_length=200)),
                ('categoria', models.CharField(blank=True, choices=[('c', 'Conferencia'), ('s', 'Seminario'), ('g', 'Congreso'), ('u', 'Curso')], default='c', help_text='Categorìa del evento', max_length=1)),
                ('lugar', models.CharField(blank=True, help_text='Lugar del evento', max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('tipo', models.CharField(blank=True, choices=[('p', 'Presencial'), ('v', 'Virtual'), ('g', 'Congreso'), ('u', 'Curso')], default='c', help_text='Tipo de evento', max_length=1)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]