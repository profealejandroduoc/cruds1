from django.shortcuts import render
from datetime import date
from .models import Persona, Perfil
from django.shortcuts import get_object_or_404, redirect
from .forms import PersonaForm, UpdatePersonaForm, UserForm, PerfilForm
from os import remove, path
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages


def perfil(request):
    form=PerfilForm()
    usr=request.user
    print("EL ID", usr.id)

    datos={
        "form":form
    }


 
    existe=Perfil.objects.filter(usuario=usr).exists()
    print(existe)
   

    if request.method=="POST":
        form=PerfilForm(data=request.POST)
        if form.is_valid():
            #form.save()
            if Perfil.objects.filter(usuario=usr).exists():
                perfil=get_object_or_404(Perfil, usuario=usr)
                #cargar datos al prinicpio de la página
            else:
                perfil=Perfil()

            perfil.usuario_id=int(usr.id)
            perfil.telefono=form.cleaned_data["telefono"]
            perfil.direccion=form.cleaned_data["direccion"]
            perfil.save()

            datos["alerta"]="Datos modificados exitosamente"
                

   
    return render(request,'crud/perfil.html', datos)


def crearcuenta(request):
    form=UserForm()

    if request.method=="POST":
        form=UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            #mejor crear el perfil
            #perfil=Perfil()
            #perfil.usuario=form.cleaned_data["username"]
            #perfil.save()

            return redirect(to="login")

    datos={
        "form":form
    }
    return render(request,'registration/crearcuenta.html', datos)

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

