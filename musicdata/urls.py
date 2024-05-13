# from django.urls import include, path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('song/<int:pk>', views.song, name='song'),
#     path('spec/<int:pk>', views.spec, name='spec'),
#     path('list/<str:type>', views.list, name='list'),
#     path('poslist/', views.poslist, name='poslist'),
#     path('delete/<int:pk>', views.delete, name='delete'),
# ]

from django.urls import include, path
from . import views
from . import api

urlpatterns = [
   path('', views.SongList.as_view(), name='index'),
   path('song/<int:pk>', views.SongDetail.as_view(), name='song'),
   path('list/<str:album>', views.SongList.as_view(), name='list'),
   path('keylist/<str:type>', views.SongList.as_view(), name='keylist'),
   path('delete/<int:pk>', views.SongDelete.as_view(), name='delete'),
   path('create_album/', views.create_album, name='create'),
   path('create_spec/', views.create_spec, name='create_spec'),
   path('create_song/', views.SongCreate.as_view(), name='create_song'),
   path('update/<int:pk>', views.SongUpdate.as_view(), name='update'),
   path('api/song/<int:pk>/', api.SongDetails.as_view(), name='song_api'), 
   path('api/songs', api.SongList.as_view(), name='songs_api'), 
   path('api/album/<int:pk>/', api.AlbumDetails.as_view(), name='album_api'),
   path('api/albums', api.AlbumList.as_view(), name='albums_api'),
   path('api/spec/<int:pk>/', api.SpecDetails.as_view(), name='spec_api'),
   path('api/specs', api.SpecList.as_view(), name='specs_api'),
   path('app/', views.SPA, name='spa'),
]