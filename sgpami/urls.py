from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('agenda_unificada/', include('agenda.urls')),
    path('mapas/',include('prestadores.urls')), 
    path('mapa/',include('mapa.urls')),
    path('menu/',include('menudigital.urls')),
    path('mapa-instituciones/', include('mapa.urls')), 
    path('formulario/',include('Formulario.urls')), 
    path(r'^.well-known/acme-challenge/', include('letsencrypt.urls'))
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
