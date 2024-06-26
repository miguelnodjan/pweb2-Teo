from django.shortcuts import render, get_list_or_404, redirect
from .models import Persona
from .forms import PersonaForm, RawPersonaForm
from django.views.generic import ListView


# Create your views here.
def personasAnotherCreateView(request):
    form = RawPersonaForm()#request.GET
    if request.method == 'POST':
        form = RawPersonaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Persona.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context ={
        'form': form,
    }
    return render(request, 'personas/personasCreate.html', context)

def personaTestView(request):
    obj = Persona.objects.get(id = 1)
    context ={
        'objeto' : obj,
    }
    return render(request, 'personas/descripcion.html', context)

def personaCreateView(request):
    initialNombres={
        'nombre': 'sin nombre'
    }
    form = PersonaForm(request.POST or None, initial= initialNombres)
    if form.is_valid():
        form.save()
        form = PersonaForm()
    
    context={
        'form' : form,
    }
    return render(request, 'personas/personasCreate.html', context)
def searchForHelp   (request):
    return render(request, 'personas/search.html', {})

def personasShowObject(request, myID):
    ibj = Persona.objects.get(id = myID)
    context={
        'objeto' : ibj

    }
    return render(request, 'personas/descripcion.html', context)
def PersonaListView(ListView):
    model= Persona
def personasDeleteView(request, myID):
    obj = get_list_or_404(Persona, id=myID)
    if request.method == 'POST':
        print('Lo borró')
        obj.delete()
        return redirect('../../')
    context ={
        'objeto' : obj,
    }
    return render(request, 'personas/personasBorrar.html', context)
