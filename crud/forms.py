from django import forms
from .models import Persona
from .enumeraciones import *

class PersonaForm(forms.ModelForm):

    rut=forms.CharField(help_text="Ingrese rut sin puntos y con guión")
    fnacto=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Persona
        fields = ['rut','nombre','apellido','foto','fnacto','correo','sexo']
