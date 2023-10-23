from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('games', views.GameList.as_view(), name='game_list'),
    
]