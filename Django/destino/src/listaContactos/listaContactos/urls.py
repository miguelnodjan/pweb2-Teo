"""
URL configuration for listaContactos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio.views import anotherView, myHomeView
from personas.views import personaTestView, personaCreateView, searchForHelp, personasAnotherCreateView, personasShowObject

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", myHomeView, name='Página de inicio'),
    path('another/', anotherView, name='otro'),
    path('persona/', personaTestView, name ='testViewPersona'),
    path('agregar/', personaCreateView, name ='createPersona'),
    path('buscar/', searchForHelp, name ='buscar'),
    path('anotherAgregar/', personasAnotherCreateView, name ='otroCreatePersona'),
    path('personas/<int:myID>/', personasShowObject, name = 'browsing')
]
