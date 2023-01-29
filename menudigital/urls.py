from django.urls import path
from .views import menu

urlpatterns = [
    path('menu/',menu.as_view(), name='menues'),
]
