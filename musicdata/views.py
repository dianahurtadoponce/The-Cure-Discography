from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from .forms import *

def SPA(request):
  return render(request, 'musicdata/spa.html')

class SongList(ListView):
  model = Songs
  context_object_name = 'master_songs'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['master_songs'] = Songs.objects.all()
    if 'album' in self.kwargs:
      if "Pornography" in self.kwargs['album'] or "The Top" in self.kwargs['album'] or "Concert - The Cure Live" in self.kwargs['album'] or "The Head On The Door" in self.kwargs['album'] or "Kiss Me Kiss Me Kiss Me" in self.kwargs['album'] or "Disintegration (Deluxe Edition [Remastered])" in self.kwargs['album'] or "Mixed Up (Remastered 2018/Deluxe Edition)" in self.kwargs['album'] or "Wish" in self.kwargs['album'] or "Paris" in self.kwargs['album'] or "Show" in self.kwargs['album'] or "Wild Mood Swings" in self.kwargs['album'] or "Bloodflowers" in self.kwargs['album'] or "The Cure" in self.kwargs['album'] or "Hypnagogic States" in self.kwargs['album'] or "4:13 Dream" in self.kwargs['album'] or "Bestival Live 2011" in self.kwargs['album']: 
        context['songs'] = Songs.objects.filter(album__exact=self.kwargs['album'])
    if 'type' in self.kwargs:
      if "major" in self.kwargs['type'] or "minor" in self.kwargs['type']: 
        context['specs'] = Specs.objects.filter(mode__exact=self.kwargs['type'])
    return context
  
  def get_template_names(self):
    if 'album' in self.kwargs:
      if "Pornography" in self.kwargs['album'] or "The Top" in self.kwargs['album'] or "Concert - The Cure Live" in self.kwargs['album'] or "The Head On The Door" in self.kwargs['album'] or "Kiss Me Kiss Me Kiss Me" in self.kwargs['album'] or "Disintegration (Deluxe Edition [Remastered])" in self.kwargs['album'] or "Mixed Up (Remastered 2018/Deluxe Edition)" in self.kwargs['album'] or "Wish" in self.kwargs['album'] or "Paris" in self.kwargs['album'] or "Show" in self.kwargs['album'] or "Wild Mood Swings" in self.kwargs['album'] or "Bloodflowers" in self.kwargs['album'] or "The Cure" in self.kwargs['album'] or "Hypnagogic States" in self.kwargs['album'] or "4:13 Dream" in self.kwargs['album'] or "Bestival Live 2011" in self.kwargs['album']:
        return('musicdata/list.html')
    if 'type' in self.kwargs:
      if "major" in self.kwargs['type'] or "minor" in self.kwargs['type']:
        return('musicdata/keylist.html')
    return 'musicdata/index.html'

class SongDetail(DetailView):
  model = Songs
  context_object_name = 'song'
  template_name = 'musicdata/song.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['master_songs'] = Songs.objects.all()
    return context

def song(request, pk):
 song = Songs.objects.get(pk=pk)
 song.access += 1
 print("Song record:", pk, "access count:", str(song.access))
 song.save()
 master_songs = Songs.objects.all()
 return render(request, 'musicdata/song.html', {'song': song, 'master_songs': master_songs})

class SongDelete(DeleteView):
  model = Songs
  success_url = "/"
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['master_songs'] = Songs.objects.all()
    return context
  
class SongUpdate(UpdateView):
  model = Songs
  success_url = "/"
  fields = ['song_id', 'album', 'name', 'track_popularity']
  template_name_suffix = '_update_form'
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['master_songs'] = Songs.objects.all()
    return context

def create_album(request):
  master_songs = Songs.objects.all()
  if request.method == 'POST':
    form = AlbumsForm(request.POST)
    if form.is_valid():
      album = Albums()
      album.album_name = form.cleaned_data['album_name']
      albumnam = form.save()
      return HttpResponseRedirect('/create_album/')
    else:
      return render(request, 'musicdata/album.html', {'error':"failed", 'master_songs': master_songs, 'form': form})
  else:
    albums = Albums.objects.all()
    form = AlbumsForm()
    return render(request, 'musicdata/album.html', {'form': form, 'albums': albums, 'master_songs': master_songs})
  
def create_spec(request):
  master_songs = Songs.objects.all()
  if request.method == 'POST':
    form = SpecsForm(request.POST)
    if form.is_valid():
      spec = Specs()
      spec.song_name = form.cleaned_data['song_name']
      specnam = form.save()
      return HttpResponseRedirect('/create_spec/')
    else:
      return render(request, 'musicdata/spec.html', {'error':"failed", 'master_songs': master_songs, 'form': form})
  else:
    specs = Specs.objects.all()
    form = SpecsForm()
    return render(request, 'musicdata/spec.html', {'form': form, 'specs': specs, 'master_songs': master_songs})
  
class SongCreate(CreateView):
  model = Songs
  template_name = 'musicdata/create_song.html'
  form_class = SongsForm
  success_url = "/create_song/"
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['master_songs'] = Songs.objects.all()
    return context
