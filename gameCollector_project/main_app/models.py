from django.db import models
from django.urls import reverse

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return self.name

   

