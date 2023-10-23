from django.shortcuts import render
# Models import
from .models import Game

# CBV imports
from django.views.generic import ListView


# Create your views here.

#Home Route
def home(request):
    return render(request, 'home.html')

# Game CBV
class GameList(ListView):
    model = Game
    template_name = "games/game_list.html"






