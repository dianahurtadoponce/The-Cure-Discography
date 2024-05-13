import os
import sys
import django
import csv
from collections import defaultdict

sys.path.append("/home/dkhp1/midterm/awd-midterm/discrography")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'discrography.settings')
django.setup()

from musicdata.models import *

data_file = '/home/dkhp1/midterm/awd-midterm/discrography/thecure_discography.csv'

albums = set()
specs = set()
songs = defaultdict(list)

with open(data_file) as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  header = csv_reader.__next__()
  for row in csv_reader:
   albums.add((row[1],row[2],row[3],row[4]))
   specs.add((row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12],
              row[13], row[14], row[15], row[16], row[17],row[18]))
   songs[row[0]] = (row[1],row[5],row[19])

Albums.objects.all().delete()
Songs.objects.all().delete()
Specs.objects.all().delete()

albums_rows = {}
specs_rows = {}
songs_rows = {}

for entries in albums:
  row = Albums.objects.create(album_name=entries[0], release=entries[2], cover=entries[1], popularity=entries[3])
  row.save()
  albums_rows[entries[0]] = row

for entries in specs:
  row = Specs.objects.create(song_name=entries[0], duration=entries[13], danceability=entries[1], energy=entries[2], key=entries[3],
                             loudness=entries[4], mode=entries[5], speechiness=entries[6], acousticness=entries[7],
                             instrumentalness=entries[8], liveness=entries[9], valence=entries[10], tempo=entries[11],
                             time_signature=entries[12])
  row.save()
  specs_rows[entries[0]] = row

for song_id, data in songs.items():
  row = Songs.objects.create(song_id=song_id, album = albums_rows[data[0]],
                            name=specs_rows[data[1]], track_popularity=data[2])
  row.save()
