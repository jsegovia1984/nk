from django.shortcuts import render
from django.views.generic.list import ListView
from .models import postres

# Create your views here.
# def menu(request):
#     data={
#         "titulo":"Menu bar 1",
#     }

#     return(render(request,"menu.html",data))

class menu(ListView):
    model = postres
    template_name = 'menu.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(self, **kwargs)
    #     context['postres'] =  postres.objects.all()
    #     return context

 