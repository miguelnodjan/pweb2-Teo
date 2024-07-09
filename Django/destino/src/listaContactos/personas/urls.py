
from django.urls import path
from personas.views import personaTestView, personaCreateView, personasDeleteView, personasAnotherCreateView, personasShowObject, personasListView
from .views import PersonaListView
app_name = 'personas'
urlpatterns = [
    path('', PersonaListView.as_view(), name = 'persona-list'),
    path('persona/', personaTestView, name ='testViewPersona'),
    path('agregar/', personaCreateView, name ='createPersona'),
    path('anotherAgregar/', personasAnotherCreateView, name ='otroCreatePersona'),
    path('personas/<int:myID>/', personasShowObject, name = 'browsing'),
    path('personas/', personasListView, name = 'listing'),
    path('personas/<int:myID>/delete/', personasDeleteView, name = 'deleting'),
]
