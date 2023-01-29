from django.urls import path
#from Formulario import views
from .views import inicio

urlpatterns = [
      path('',inicio, name='inicio')
]
