from django.db import models
from django.utils import timezone
from rest_framework.authtoken.admin import User


class Genre(models.Model):
    name = models.CharField(max_length=50)
    genre_pic = models.ImageField(upload_to="genres", default="default.jpeg")


class Author(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey('Song', on_delete=models.CASCADE)


class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey('Song', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()


class Song(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Song name")
    text = models.TextField()
    song_pic = models.ImageField(upload_to="song_pic", blank=False)
    song = models.FileField(upload_to="songs")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    author = models.ManyToManyField(Author)
    playtime = models.CharField(max_length=10, default="0.00")
    created_at = models.DateTimeField(verbose_name='Created At', default=timezone.now)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    year = models.DateField()



