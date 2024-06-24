from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'edad', 'donador']
    
    def clean_nombres(self, *args, **kwargs):
        print('Paso')
        name = self.cleaned_data.get('nombre')
        if name.isTitle():
            return name
        else:
            raise forms.ValidationError('El nombre debe empezar con mayúscula')

class RawPersonaForm(forms.Form):
    nombre = forms.CharField(
        widget= forms.Textarea(
            attrs={
                'placeholder':'Solo tu nombre por favor',
                'id': 'nombreID',
                'class' : 'special',
                'cols' : '10',
            }
        )
    )
    apellido = forms.CharField()
    edad = forms.IntegerField(initial=20)
    donador = forms.BooleanField()