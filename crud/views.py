from django.shortcuts import render
from datetime import date
from .models import Persona
from django.shortcuts import get_object_or_404, redirect
from .forms import PersonaForm, UpdatePersonaForm
from os import remove, path
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.models import User



def crearcuenta(request):
    return render(request,'registration/crearcuenta.html')

def cerrar_sesion(request):
    logout(request)
    return redirect(to='index')

# Create your views here.
def index(request):
    fecha=date.isoformat(date.today())
    texto="Para traer los datos desde la vista se debe enviar a través del contexto de datos"
    lista=['Alfajor', 'Poleron', 'Paraguas','Gorro','Cruz con Micrófono']
    elementos=len(lista)

    datos={
        "fecha":fecha,
        "msg":texto,
        "lista":lista,
        "items":elementos
    }
    return render(request,'crud/index.html', datos)

def personas(request):
    people=Persona.objects.all() #queryset
    
    datos={
        "personas":people
    }
    return render(request,'crud/personas.html', datos)

def crearpersona(request):
    
    form=PersonaForm()

   

    if request.method=="POST":
        form=PersonaForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to="personas")
            #Redirigir
    
    datos={
        "form":form
    }

    return render(request,'crud/crearpersona.html',datos)


def detallepersona(request,id):
    persona=get_object_or_404(Persona,rut=id)

    datos={
        "persona":persona
    }

    return render(request,'crud/detallepersona.html',datos)


def modificar(request, id):
    persona=get_object_or_404(Persona,rut=id)
    form=UpdatePersonaForm(instance=persona)
    
    if request.method=="POST":
        form=UpdatePersonaForm(data=request.POST,files=request.FILES,instance=persona)
        if form.is_valid():
            form.save()
            return redirect(to="personas")
    
    
    datos={
        "form":form,
        "persona":persona
    }
    
    
    return render(request,'crud/modificar.html',datos)


def eliminar(request,id):
    persona=get_object_or_404(Persona, rut=id)
    
    if request.method=="POST":
        
        #from os import remove, path
        #from django.conf import settings
        remove(path.join(str(settings.MEDIA_ROOT).replace('/media',''))+persona.foto.url)
        persona.delete()
        return redirect(to="personas")
        
    datos={
        "persona":persona
    }
    
    return render(request,'crud/eliminar.html', datos)

