from django.db import models

# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=100)
    genre  = models.CharField(max_length=100)
    logo   = models.CharField(max_length=1000)
    album_title = models.CharField(max_length=250)

    def __str__(self):
        return self.artist +' - ' + self.album_title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=100)
    song_title = models.CharField(max_length=150)
    is_favourite = models.BooleanField(default= False)



    def __str__(self):
        return self.song_title



