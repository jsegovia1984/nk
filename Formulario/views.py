from django.shortcuts import render
# Create your views here.
from .models import Persona
from .forms import PersonaForm
from django.http import HttpResponse
import json

def inicio(request):
#    TodosLosPost = Post.objects.all()
    data = {
	'Form': PersonaForm()
    }
    
    if request.method == "POST":
        formulario = PersonaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Gracias!, Se realizó la inscripción correctamente"
        else:
            data["Form"] = formulario

    return render(request, 'inicio.html', data)
