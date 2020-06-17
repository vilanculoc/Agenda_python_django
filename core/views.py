from django.shortcuts import render, redirect
from core.models import Evento
# Create your views here.

#Redireccionar para agenda quando nada for informado no index. a outra parte estano url path
# def index(request):
#     return redirect('/agenda/')


def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.all()
    #evento = Evento.objects.filter(usuario=usuario)   # retorna os eventos do usuario logado, sessao login
    response = {'eventos':evento}
    return render(request, 'agenda.html', response)

