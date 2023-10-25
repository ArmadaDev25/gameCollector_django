from django.shortcuts import render
# Models import
from .models import Game

# CBV imports
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


# Create your views here.

# Home Route
def home(request):
    return render(request, 'home.html')

# Game CBV
class GameList(ListView):
    model = Game
    template_name = "games/game_list.html"

class GameDetail(DetailView):
    model = Game
    template_name = "games/game_detail.html"

class GameCreate(CreateView):
    model = Game
    template_name = "games/game_form.html"
    fields = "__all__"

class GameUpdate(UpdateView):
    model = Game
    template_name = "games/game_form.html"
    fields = "__all__"

class GameDelete(DeleteView):
    model = Game
    template_name = "games/game_confirm_delete.html"
    success_url = '/games'





