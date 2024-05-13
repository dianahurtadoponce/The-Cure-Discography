from django.contrib import admin
from.models import *

# Register your models here.

class AlbumsAdmin(admin.ModelAdmin):
    list_display = ('album_name', 'release', 'cover', 'popularity')

class SpecsAdmin(admin.ModelAdmin):
    list_display = ('song_name', 'duration', 'danceability', 'energy',  'key', 'loudness', 'mode', 'speechiness', 'acousticness', 
                     'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature')

class SongsAdmin(admin.ModelAdmin):
    list_display = ('song_id', 'album', 'name', 'track_popularity')



admin.site.register(Albums, AlbumsAdmin)
admin.site.register(Specs, SpecsAdmin)
admin.site.register(Songs, SongsAdmin)
