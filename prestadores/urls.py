from django.urls import path
from .views import home,primernivel,segundonivel,diagnostico,ecodoppler,kinesiologia,agenda,menu

urlpatterns = [
    path('', home, name='home'),
    path('primernivel/', primernivel, name='primer'),   
    path('segundonivel/', segundonivel, name='segundo'),
    path('diagnostico/', diagnostico, name='diagnostico'),
    path('ecodoppler/', ecodoppler, name='ecodoppler'),
    path('kinesiologia/', kinesiologia, name='kinesiologia'),
    path('agenda/', agenda.as_view(), name='agenda'),
]
