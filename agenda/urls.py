from django.urls import path
from .views import agenda

urlpatterns = [
      path('', agenda.as_view(), name='agenda'),

]