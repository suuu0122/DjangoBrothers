from django.shortcuts import render

from .models import Player



def index(request):
    players = Player.objects.all()
    return render(request, "arsenal_players/index.html", {"players": players})

def detail(request, player_id):
    player = Player.objects.get(id=player_id)
    return render(request, "arsenal_players/detail.html", {"player": player})