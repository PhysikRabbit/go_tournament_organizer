from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Game

def index(request):
    games_list = Game.objects.all()
    template = loader.get_template('games/index.html')
    context = {
        'games_list': games_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, game_id):
    return HttpResponse("This is game %s." % game_id)