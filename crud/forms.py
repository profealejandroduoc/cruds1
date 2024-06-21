from django import forms
from .models import Persona, Perfil
from .enumeraciones import *
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    pass

class PerfilForm(forms.ModelForm):

    class Meta:
        model=Perfil
        fields=['telefono', 'direccion']



class PersonaForm(forms.ModelForm):

    rut=forms.CharField(help_text="Ingrese rut sin puntos y con guión")
    fnacto=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de Nacimiento")
    
    class Meta:
        model = Persona
        fields = ['rut','nombre','apellido','foto','fnacto','correo','sexo']


class UpdatePersonaForm(forms.ModelForm):


    fnacto=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de Nacimiento")
    
    class Meta:
        model = Persona
        fields = ['nombre','apellido','foto','fnacto','correo','sexo']