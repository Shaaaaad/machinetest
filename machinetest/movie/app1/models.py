from django.db import models

# Create your models here.

class Movie(models.Model):
    moviename = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    year = models.CharField(max_length=100)

    def __str__(self):
        return self.moviename

class Favorites(models.Model):
    moviename = models.ForeignKey(Movie, on_delete=models.CASCADE)


    def __str__(self):
        return self.moviename