from django import forms
from .models import Persona
from .enumeraciones import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CrearUsuarioForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=['username','password1','password2','first_name','last_name', 'email']
    



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