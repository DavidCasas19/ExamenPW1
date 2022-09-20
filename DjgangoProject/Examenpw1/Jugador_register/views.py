from django.shortcuts import render,redirect
from .forms import PlayerForm
from .models import Player

from .forms import TeamForm
from .models import Team

from .forms import StadiumForm
from .models import Stadium

# Create your views here.
def menu(request):
    return render(request, "Jugador_register/menu.html")


"""Inicio de la vista de Jugador"""

def Jugador_List(request):
    context = {'Jugador_list': Player.objects.all()}
    return render(request, "Jugador_register/Jugador_list.html",context)


def Jugador_Form(request,id=0):
    if request.method == "GET":
        if id == 0:
             form = PlayerForm()
        else:
            player = Player.objects.get(pk=id)
            form = PlayerForm(instance=player)
        jls_extract_var = 'form'
        return render(request, "Jugador_register/Jugador_form.html", {jls_extract_var:form})
    else:
        if id == 0:
            form = PlayerForm(request.POST)
        else:
            player = Player.objects.get(pk=id)
            form = PlayerForm(request.POST,instance=player)
        if form.is_valid():
            form.save()
        return redirect('/Jugador/listP')



def Jugador_delete(request,id):
    player = Player.objects.get(pk=id)
    player.delete()
    return redirect('/Jugador/listP')

"""Inicio de la vista de Equipo"""

def Equipo_list(request):
    context = {'Equipo_list': Team.objects.all()}
    return render(request, "Jugador_register/Equipo_list.html",context)

def Equipo_form(request,id=0):
    if request.method == "GET":
        if id == 0:
             form = TeamForm()
        else:
            team = Team.objects.get(pk=id)
            form = TeamForm(instance=team)
        jls_extract_var = 'form'
        return render(request, "Jugador_register/Equipo_Form.html", {jls_extract_var:form})
    else:
        if id == 0:
            form = TeamForm(request.POST)
        else:
            team = Team.objects.get(pk=id)
            form = TeamForm(request.POST,instance=team)
        if form.is_valid():
            form.save()
        return redirect('/Jugador/listT')
    
def Equipo_delete(request,id):
    team = Team.objects.get(pk=id)
    team.delete()
    return redirect('/Jugador/listT')



"""Inicio de la vista de Estadio"""


def Estadio_list(request):
    context = {'Estadio_list': Stadium.objects.all()}
    return render(request, "Jugador_register/Estadio_list.html",context)

def Estadio_form(request,id=0):
    if request.method == "GET":
        if id == 0:
             form = StadiumForm()
        else:
            stadium = Stadium.objects.get(pk=id)
            form = StadiumForm(instance=stadium)
        jls_extract_var = 'form'
        return render(request, "Jugador_register/Estadio_Form.html", {jls_extract_var:form})
    else:
        if id == 0:
            form = StadiumForm(request.POST)
        else:
            stadium = Stadium.objects.get(pk=id)
            form = StadiumForm(request.POST,instance=stadium)
        if form.is_valid():
            form.save()
        return redirect('/Jugador/listE/')
    
def Estadio_delete(request,id):
    stadium = Stadium.objects.get(pk=id)
    stadium.delete()
    return redirect('/Jugador/listE')
    

 