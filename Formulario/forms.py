from django import forms

from Formulario.models import Persona

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = '__all__'
 #       widgets = {'texto':forms.TextInput(attrs = {'id':'post-formulario', 'requerid':True, 'placeholder':'Escribe tu Post'})}
