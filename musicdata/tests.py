import json
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse_lazy

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from .model_factories import *
from .serializers import *

class SongSerialiserTest(APITestCase):
   song1 = None
   songserializer = None 

   def setUp(self):
    self.song1 = SongFactory.create(pk=1, song_id="1")
    self.songserializer = SongSerializer(instance=self.song1) 
  
   def tearDown(self):
     Albums.objects.all().delete()
     Specs.objects.all().delete()
     Songs.objects.all().delete()
     AlbumFactory.reset_sequence(0)
     SpecsFactory.reset_sequence(0)
     SongFactory.reset_sequence(0)

   def test_songSerilaizer(self):
     data = self.songserializer.data
     self.assertEqual(set(data.keys()), set(['song_id', 'album', 'name', 'track_popularity'])) 

   def test_songSerilaiserSongIDIHasCorrectData(self):
     data = self.songserializer.data
     self.assertEqual(data['song_id'], 1)  

class AlbumSerialiserTest(APITestCase):
   album1 = None
   albumserializer = None 

   def setUp(self):
    self.album1 = AlbumFactory.create(pk=1, album_name="Pornography")
    self.albumserializer = AlbumSerializer(instance=self.album1) 
  
   def tearDown(self):
     Albums.objects.all().delete()
     Specs.objects.all().delete()
     Songs.objects.all().delete()
     AlbumFactory.reset_sequence(0)
     SpecsFactory.reset_sequence(0)
     SongFactory.reset_sequence(0)
     
   def test_albumSerilaizer(self):
     data = self.albumserializer.data
     self.assertEqual(set(data.keys()), set(['id', 'album_name', 'cover', 'release', 'popularity']))

   def test_albumSerilaizerAlbumNameHasCorrectData(self):
     data = self.albumserializer.data
     self.assertEqual(data['album_name'], 'Pornography')

class SpecSerialiserTest(APITestCase):
   spec1 = None
   specserializer = None 

   def setUp(self):
    self.spec1 = SpecsFactory.create(pk=1, song_name="One Hundred Years - Remastered Version")
    self.specserializer = SpecsSerializer(instance=self.spec1) 
  
   def tearDown(self):
     Albums.objects.all().delete()
     Specs.objects.all().delete()
     Songs.objects.all().delete()
     AlbumFactory.reset_sequence(0)
     SpecsFactory.reset_sequence(0)
     SongFactory.reset_sequence(0)
     
   def test_specSerilaizer(self):
     data = self.specserializer.data
     self.assertEqual(set(data.keys()), set(['id', 'song_name', 'duration', 'danceability', 'energy', 'key', 
                                             'loudness', 'mode', 'speechiness', 'acousticness', 
                                             'instrumentalness', 'liveness', 'valence', 'tempo', 
                                             'time_signature']))

   def test_specSerilaizerSongNameHasCorrectData(self):
     data = self.specserializer.data
     self.assertEqual(data['song_name'], 'One Hundred Years - Remastered Version')

class SongTest(APITestCase):
   song1 = None
   good_url = ''
   bad_url = ''
   delete_url = ''
   post_url = ''
   put_url = ''
   
   def setUp(self):
     self.song1 = SongFactory.create(pk=1, song_id=1)
    #  self.song2 = SongFactory.create(pk=2, song_id=2)
    #  self.song3 = SongFactory.create(pk=3, song_id=3) 
     self.good_url = reverse('song_api', kwargs={'pk': 1})
     self.bad_url = "/api/song/H/" 
     self.delete_url = reverse('song_api', kwargs={'pk': 1}) 
     self.post_url = reverse('song_api', kwargs={'pk': 1})
     self.put_url = reverse('song_api', kwargs={'pk': 1})
   
   def tearDown(self):
     Albums.objects.all().delete()
     Specs.objects.all().delete()
     Songs.objects.all().delete()
     AlbumFactory.reset_sequence(0)
     SpecsFactory.reset_sequence(0)
     SongFactory.reset_sequence(0) 

   def test_songDetailReturnsSuccess(self):
     response = self.client.get(self.good_url, format='json')
     response.render()
     self.assertEqual(response.status_code, 200)
     data = json.loads(response.content)
     self.assertTrue('track_popularity' in data)
     self.assertEqual(data['track_popularity'], 33) 

   def test_songDetailReturnFailOnBadPk(self):
     response = self.client.get(self.bad_url, format='json')
     self.assertEqual(response.status_code, 404) 

   def test_songDetailDeleteIsSuccessful(self):
     response = self.client.delete(self.delete_url, format='json')
     self.assertEqual(response.status_code, 204) 

   def test_songDetailPostIsSuccessful(self):
     mydata = {
    "song_id": 204,
    "album": {"id": 1,"album_name": "The Cure","cover": "https://i.scdn.co/image/34ce6c6c4fd523c5415886027f340505dafd1dc3","release": "2004-06-28","popularity": 28},
    "name": {
    "id": 1,
    "song_name": "The Figurehead - Live Paris Version",
    "duration": 446933,
    "danceability": 0.582,
    "energy": 0.395,
    "key": "A#",
    "loudness": -17.46,
    "mode": "minor",
    "speechiness": 0.0286,
    "acousticness": 0.000877,
    "instrumentalness": 0.551,
    "liveness": 0.976,
    "valence": 0.335,
    "tempo": 105.38,
    "time_signature": 4},
    "track_popularity": 33}
     response = self.client.post(self.post_url, mydata, format='json')
     self.assertEqual(response.status_code, 201) 

   def test_songDetailPutIsSuccessful(self):
     mydata = {
    "song_id": 1,
    "album": {"id": 1,"album_name": "The Cure","cover": "https://i.scdn.co/image/34ce6c6c4fd523c5415886027f340505dafd1dc3","release": "2005-06-28","popularity": 0},
    "name": {
    "id": 1,
    "song_name": "Testing",
    "duration": 0,
    "danceability": 0,
    "energy": 0,
    "key": "G",
    "loudness": 0,
    "mode": "major",
    "speechiness": 0,
    "acousticness": 0,
    "instrumentalness": 0,
    "liveness": 0,
    "valence": 0,
    "tempo": 0,
    "time_signature": 0},
    "track_popularity": 0}
     response = self.client.put(self.put_url, mydata, format='json')
     self.assertEqual(response.status_code, 200) 

class AlbumTest(APITestCase):
   album1 = None
   good_url = ''
   bad_url = ''
   delete_url = ''
   post_url = ''
   put_url = ''
   
   def setUp(self):
     self.album1 = AlbumFactory.create(pk=1, album_name= "Pornography")
    #  self.song2 = SongFactory.create(pk=2, song_id=2)
    #  self.song3 = SongFactory.create(pk=3, song_id=3)   
     self.good_url = reverse('album_api', kwargs={'pk': 1})
     self.bad_url = "/api/song/H/" 
     self.delete_url = reverse('album_api', kwargs={'pk': 1}) 
     self.post_url = reverse('album_api', kwargs={'pk': 1})
     self.put_url = reverse('album_api', kwargs={'pk': 1})

   def tearDown(self):
     Albums.objects.all().delete()
     Specs.objects.all().delete()
     Songs.objects.all().delete()
     AlbumFactory.reset_sequence(0)
     SpecsFactory.reset_sequence(0)
     SongFactory.reset_sequence(0) 

   def test_albumDetailReturnsSuccess(self):
     response = self.client.get(self.good_url, format='json')
     response.render()
     self.assertEqual(response.status_code, 200)
     data = json.loads(response.content)
     self.assertTrue('album_name' in data)
     self.assertEqual(data['album_name'], 'Pornography') 

   def test_albumDetailReturnFailOnBadPk(self):
     response = self.client.get(self.bad_url, format='json')
     self.assertEqual(response.status_code, 404) 

   def test_albumDetailDeleteIsSuccessful(self):
     response = self.client.delete(self.delete_url, format='json')
     self.assertEqual(response.status_code, 204) 
   
   def test_albumDetailPostIsSuccessful(self):
    mydata = {"id": 1,"album_name": "The Cure","cover": "https://i.scdn.co/image/34ce6c6c4fd523c5415886027f340505dafd1dc3","release": "2004-06-28","popularity": 28}
    response = self.client.post(self.post_url, mydata, format='json')
    self.assertEqual(response.status_code, 201)
  
   def test_albumDetailPuttIsSuccessful(self):
    mydata = {"id": 1,"album_name": "The Cure","cover": "https://i.scdn.co/image/34ce6c6c4fd523c5415886027f340505dafd1dc3","release": "2005-06-28","popularity": 0}
    response = self.client.put(self.put_url, mydata, format='json')
    self.assertEqual(response.status_code, 200)



class SpecTest(APITestCase):
   spec1 = None
   good_url = ''
   bad_url = ''
   delete_url = ''
   post_url = ''
   put_url = ''
   
   def setUp(self):
     self.spec1 = SpecsFactory.create(pk=1, song_name = 'One Hundred Years - Remastered Version')
    #  self.song2 = SongFactory.create(pk=2, song_id=2)
    #  self.song3 = SongFactory.create(pk=3, song_id=3) 
     self.good_url = reverse('spec_api', kwargs={'pk': 1})
     self.bad_url = "/api/spec/H/" 
     self.delete_url = reverse('spec_api', kwargs={'pk': 1}) 
     self.post_url = reverse('spec_api', kwargs={'pk': 1})
     self.put_url = reverse('spec_api', kwargs={'pk': 1})
   
   def tearDown(self):
     Albums.objects.all().delete()
     Specs.objects.all().delete()
     Songs.objects.all().delete()
     AlbumFactory.reset_sequence(0)
     SpecsFactory.reset_sequence(0)
     SongFactory.reset_sequence(0) 

   def test_specDetailReturnsSuccess(self):
     response = self.client.get(self.good_url, format='json')
     response.render()
     self.assertEqual(response.status_code, 200)
     data = json.loads(response.content)
     self.assertTrue('song_name' in data)
     self.assertEqual(data['song_name'], 'One Hundred Years - Remastered Version') 

   def test_specDetailReturnFailOnBadPk(self):
     response = self.client.get(self.bad_url, format='json')
     self.assertEqual(response.status_code, 404) 

   def test_specDetailDeleteIsSuccessful(self):
     response = self.client.delete(self.delete_url, format='json')
     self.assertEqual(response.status_code, 204) 
   
   def test_specDetailPostIsSuccessful(self):
    mydata = {
    "id": 1,
    "song_name": "The Figurehead - Live Paris Version",
    "duration": 446933,
    "danceability": 0.582,
    "energy": 0.395,
    "key": "A#",
    "loudness": -17.46,
    "mode": "minor",
    "speechiness": 0.0286,
    "acousticness": 0.000877,
    "instrumentalness": 0.551,
    "liveness": 0.976,
    "valence": 0.335,
    "tempo": 105.38,
    "time_signature": 4}
    response = self.client.post(self.post_url, mydata, format='json')
    self.assertEqual(response.status_code, 201)

   def test_specDetailPutIsSuccessful(self):
    mydata = {
    "id": 1,
    "song_name": "The Figurehead - Live Paris Version",
    "duration": 0,
    "danceability": 0,
    "energy": 0,
    "key": "G",
    "loudness": 0,
    "mode": "major",
    "speechiness": 0,
    "acousticness": 0,
    "instrumentalness": 0,
    "liveness": 0,
    "valence": 0,
    "tempo": 0,
    "time_signature": 0}
    response = self.client.put(self.put_url, mydata, format='json')
    self.assertEqual(response.status_code, 200)


class SongListTest(APITestCase):
   good_url = ''

   
   def setUp(self):
     self.good_url = '/api/songs'

   def tearDown(self):
     Albums.objects.all().delete()
     Specs.objects.all().delete()
     Songs.objects.all().delete()
     AlbumFactory.reset_sequence(0)
     SpecsFactory.reset_sequence(0)
     SongFactory.reset_sequence(0) 

   def test_songListReturnsSuccess(self):
     response = self.client.get(self.good_url, format='json')
     response.render()
     self.assertEqual(response.status_code, 200)

class AlbumListTest(APITestCase):
   good_url = ''

   
   def setUp(self):
     self.good_url = '/api/albums'

   def tearDown(self):
     Albums.objects.all().delete()
     Specs.objects.all().delete()
     Songs.objects.all().delete()
     AlbumFactory.reset_sequence(0)
     SpecsFactory.reset_sequence(0)
     SongFactory.reset_sequence(0) 

   def test_songListReturnsSuccess(self):
     response = self.client.get(self.good_url, format='json')
     response.render()
     self.assertEqual(response.status_code, 200)

class SpecListTest(APITestCase):
   good_url = ''

   
   def setUp(self):
     self.good_url = '/api/specs'

   def tearDown(self):
     Albums.objects.all().delete()
     Specs.objects.all().delete()
     Songs.objects.all().delete()
     AlbumFactory.reset_sequence(0)
     SpecsFactory.reset_sequence(0)
     SongFactory.reset_sequence(0) 

   def test_songListReturnsSuccess(self):
     response = self.client.get(self.good_url, format='json')
     response.render()
     self.assertEqual(response.status_code, 200)
