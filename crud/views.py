from django.shortcuts import render
from datetime import date

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