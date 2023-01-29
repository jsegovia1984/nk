from django.urls import path
from .views import MapaDetailView,map_json,MapaDetailViewIOMA,MapaDetailViewBasicas,MapaDetailViewACiviles,ACivilesdetalle,MapaDetailViewCasos

app_name = 'mapa'

urlpatterns = [
      path('map_json/',map_json, name='map'),
      path('basicas/',MapaDetailViewBasicas.as_view(), name='mapas-basicas'),
      path('casos/',MapaDetailViewCasos.as_view(), name='casos-de-gestion'),
      path('ioma/',MapaDetailViewIOMA.as_view(), name='mapa-ioma-prestadores'),  
      path('asociaciones_civiles/',MapaDetailViewACiviles.as_view(), name='mapa-asociaciones-civiles'),
      path('asociaciones_civiles_detail/', ACivilesdetalle.as_view(), name='detalleac'),
      path('',MapaDetailView.as_view(), name='mapas-instituciones'),



]