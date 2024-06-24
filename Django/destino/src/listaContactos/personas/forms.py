from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'edad', 'donador']

class RawPersonaForm(forms.Form):
    nombre = forms.CharField(label= "Your Name")
    apellido = forms.CharField()
    edad = forms.IntegerField(initial=20)
    donador = forms.BooleanField()