from django import forms
from django.forms import ModelForm
from .models import *

class AlbumsForm(ModelForm):
  class Meta:
     model = Albums
     fields = ['album_name', 'cover', 'release', 'popularity']
  def clean(self):
    cleaned_data = super(AlbumsForm, self).clean()
    popularity = cleaned_data.get("popularity")
    if not isinstance(popularity, int):
      raise forms.ValidationError("Popularity must be an integer")
    return(cleaned_data)

class SongsForm(ModelForm):
   class Meta:
     model = Songs
     fields = ['song_id', 'album', 'name', 'track_popularity']
   def clean(self):
    cleaned_data = super(SongsForm, self).clean()
    popularity = cleaned_data.get("track_popularity")
    if not isinstance(popularity, int):
      raise forms.ValidationError("Track Popularity must be an integer")
    return(cleaned_data)
   
class SpecsForm(ModelForm):
  class Meta:
     model = Specs
     fields = ['song_name', 'duration', 'danceability', 'energy', 'key', 
               'loudness', 'mode', 'speechiness', 'acousticness', 
               'instrumentalness', 'liveness', 'valence', 'tempo', 
               'time_signature' ]
  def clean(self):
    cleaned_data = super(SpecsForm, self).clean()
    mode = cleaned_data.get("mode")
    if not mode == 'major' and not mode == 'minor' :
      raise forms.ValidationError("Mode must be major or minor")
    return(cleaned_data)