from django.db.models.query import QuerySet
from agenda.models import agenda

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

class agenda(ListView):
    model = agenda
    template_name = 'agenda.html'

    def get_queryset(self):
        QuerySet = self.model.objects.filter()
        return QuerySet


