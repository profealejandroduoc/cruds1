from django import forms
from .models import Persona, User
from .enumeraciones import *
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=['username','rut','first_name','last_name','email','direccion','password1','password2']

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