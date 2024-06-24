from django import forms
from .models import Persona

class PersonaForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    donador = forms.BooleanField()
