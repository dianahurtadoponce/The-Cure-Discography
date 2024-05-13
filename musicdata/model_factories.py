import factory
from random import randint
from random import choice
from django.test import TestCase
from django.conf import settings
from django.core.files import File

from .models import *
class AlbumFactory(factory.django.DjangoModelFactory):
    album_name= "Pornography"
    cover = "https://i.scdn.co/image/fbec42025b461d54853ba6431f4eaaaa69e5a9e1"
    release = "1982-05-03"
    popularity = 34
    class Meta:
       model = Albums

class SpecsFactory(factory.django.DjangoModelFactory):
    song_name = 'One Hundred Years - Remastered Version'
    duration = 401000
    danceability = 0.436
    energy = 0.881
    key = 'G'
    loudness = -5.998
    mode = choice(['Major', 'Minor'])
    speechiness = 0.0439
    acousticness = 0.00123
    instrumentalness = 0.509
    liveness = 0.108
    valence = 0.262
    tempo = 132.59
    time_signature = 4
    class Meta:
       model = Specs

class SongFactory(factory.django.DjangoModelFactory):
    song_id = 1
    album =  factory.SubFactory(AlbumFactory)
    name = factory.SubFactory(SpecsFactory)
    track_popularity = 33
    access = 0
    class Meta:
        model = Songs