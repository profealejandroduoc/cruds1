from django.shortcuts import render
from datetime import date
from .models import Persona
from django.shortcuts import get_object_or_404, redirect
from .forms import PersonaForm

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