from django.contrib import admin
from .models import Perfil, Persona, Mascota

class AdmPersona(admin.ModelAdmin):
    list_display= ['rut','nombre','apellido','foto','fnacto','correo','sexo']
    #list_editable=['nombre','apellido','fnacto','correo','sexo']
    list_filter=['sexo']


class AdmMascota(admin.ModelAdmin):
    list_display=['id','nombre','tipo','subtipo','edad', 'propietario']
    list_editable=['nombre','tipo','edad','subtipo', 'propietario']
    list_filter=['propietario','tipo']

class AdmPerfil(admin.ModelAdmin):
    list_display=['usuario','telefono', 'direccion']


# Register your models here.
admin.site.register(Persona, AdmPersona)
admin.site.register(Mascota,AdmMascota)
admin.site.register(Perfil,AdmPerfil)