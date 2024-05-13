from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import *

class AlbumSerializer(serializers.ModelSerializer):
   class Meta:
      model = Albums
      fields = ['id', 'album_name', 'cover', 'release', 'popularity']

class SpecsSerializer(serializers.ModelSerializer):
   class Meta:
      model = Specs
      fields = ['id', 'song_name', 'duration', 'danceability', 'energy', 'key', 
               'loudness', 'mode', 'speechiness', 'acousticness', 
               'instrumentalness', 'liveness', 'valence', 'tempo', 
               'time_signature' ]

class SongSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
   album = AlbumSerializer()
   name = SpecsSerializer()
   class Meta:
     model = Songs
     fields = ['song_id', 'album', 'name', 'track_popularity']
   def create(self, validated_data):
      album_data = self.initial_data.get('album')
      name_data = self.initial_data.get('name')
      songs = Songs(**{**validated_data, 
                     'album':Albums.objects.get(pk=album_data['id']),
                     'name':Specs.objects.get(pk=name_data['id'])})
      songs.save()
      return songs

class SongListSerializer(serializers.ModelSerializer):
   class Meta:
     model = Songs
     fields = ['id', 'song_id', 'name', 'track_popularity'] 

class AlbumListSerializer(serializers.ModelSerializer):
   class Meta:
     model = Albums
     fields = ['id', 'album_name', 'release'] 

class SpecListSerializer(serializers.ModelSerializer):
   class Meta:
     model = Specs
     fields = ['id', 'song_name', 'key'] 