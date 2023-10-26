from django.db import models
from django.urls import reverse

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('game_detail', kwargs={'pk':self.id})

class NewContent(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField('Release Date')

    # Model that NewContent will be attacted to 
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for game_id: {self.game_id} @{self.url}"
    

   

