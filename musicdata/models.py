from django.db import models


# Create your models here.

class Albums(models.Model):
    album_name= models.CharField(max_length=256, null=False, blank=False, unique=True)
    cover = models.URLField(max_length= 200)
    release = models.DateField(null=False, blank=True)
    popularity = models.IntegerField(null=False, blank=True, default=0)

    def __str__(self):
        return self.album_name

class Specs(models.Model):
    song_name = models.CharField(max_length=256, null=False, blank=False, unique=True)
    duration = models.IntegerField(null=False, blank=True, default=0)
    danceability = models.FloatField(null=False, blank=True)
    energy = models.FloatField(null=False, blank=True)
    key = models.CharField(max_length=2)
    loudness = models.FloatField(null=False, blank=True)
    MODE_CHOICES = [('major', 'major'), ('minor','minor')]
    mode = models.CharField(max_length=256, choices=MODE_CHOICES, null=False, blank=False)
    speechiness = models.FloatField(null=False, blank=True)
    acousticness = models.FloatField(null=False, blank=True)
    instrumentalness = models.FloatField(null=False, blank=True)
    liveness = models.FloatField(null=False, blank=True)
    valence = models.FloatField(null=False, blank=True)
    tempo = models.FloatField(null=False, blank=True)
    time_signature = models.IntegerField(null=False, blank=True)
    def __str__(self):
        return self.song_name

class Songs(models.Model):
    song_id = models.IntegerField(null=False, blank=False,  db_index=True)
    album =  models.ForeignKey(Albums, to_field='album_name', on_delete=models.CASCADE)
    name = models.ForeignKey(Specs, to_field='song_name', on_delete=models.CASCADE)
    track_popularity = models.IntegerField(null=False, blank=True, default=0)
    access = models.IntegerField(null=False, blank=False, default=0)
