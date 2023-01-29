from django.db.models.query import QuerySet
from agenda.models import agenda
from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView

def home(request):
    return render(request,'index.html')

def primernivel(request):
    return render(request,'PrimerNivel.html')

def segundonivel(request):
    return render(request,'SegundoNivel.html')

def diagnostico(request):
    return render(request,'Diagnosticoporimagen.html')

def kinesiologia(request):
    return render(request,'kinesiologia.html')

def ecodoppler(request):
    return render(request,'ecodoppler.html')

def menu(request):
    return render(request,'menu.html')


class agenda(ListView):
    model = agenda
    template_name = 'agenda.html'

    def get_queryset(self):
        QuerySet = self.model.objects.filter()
        return QuerySet


