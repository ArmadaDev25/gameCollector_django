from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)
    year = models.IntegerField()
    