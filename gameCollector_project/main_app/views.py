from django.shortcuts import render, redirect
# Models import
from .models import Game, Photo, NewContent, Features

# CBV imports
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Forms Imports
from .forms import NewContentForm

#Imports for photo aws
import uuid
import boto3
import os # to access .env keys

# Create your views here.

# Home Route
def home(request):
    return render(request, 'home.html')

def GameDetail(request, pk):
    game = Game.objects.get(id=pk)
    addcontentform = NewContentForm()
    return render(request, 'games/game_detail.html',
    {
        'game' : game,
        'addcontentform' : addcontentform

    })



# Photo View
def add_photo(request, game_id):
    photo_file = request.FILES.get('photo_file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.')]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f'{os.environ["S3_BASE_URL"]}{bucket}/{key}'
            Photo.objects.create(url=url, game_id=game_id)
        except Exception as e:
            print('An Error Occured Uploading The File to S3')
            print(e)
    return redirect('game_detail', pk=game_id)




# Game CBV
class GameList(ListView):
    model = Game
    template_name = "games/game_list.html"

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

#Features CBV
class FeatureList(ListView):
    model = Features
    template_name = "features/features_list.html"

class FeatureCreate(CreateView):
    model = Features
    fields = "__all__"
    template_name = "features/features_form.html"

class FeatureDetail(DetailView):
    model = Features
    template_name = "features/features_detail.html"



def add_content(request, pk):
    form = NewContentForm(request.POST)
    if form.is_valid():
        new_content = form.save(commit=False)
        new_content.game_id = pk
        new_content.save()
    return redirect('game_detail', pk=pk)





