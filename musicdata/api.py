from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from rest_framework import generics
from rest_framework import mixins 
from .models import *
from .serializers import *

# @api_view(['GET', 'POST'])
# def gene_detail(request, pk):
#   if request.method == 'POST':
#     serializer = GeneSerializer(data=request.data)
#     if serializer.is_valid():
#        serializer.save()
#        return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
  
#   try:
#     gene = Gene.objects.get(pk=pk)
#   except Gene.DoesNotExist:
#       return HttpResponse(status=404) 
#   if request.method == 'GET':
#      serializer = GeneSerializer(gene)
#      return Response(serializer.data)
#   elif request.method == 'DELETE':
#      gene.delete()
#      return Response(status=status.HTTP_204_NO_CONTENT)
#   elif request.method == 'PUT':
#      serializer = GeneSerializer(gene, data=request.data)
#      if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SongDetails(mixins.CreateModelMixin, 
                  mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                  mixins.DestroyModelMixin, generics.GenericAPIView):
   queryset = Songs.objects.all()
   serializer_class = SongSerializer
   def post(self, request, *args, **kwargs):
     return self.create(request, *args, **kwargs)
   def get(self, request, *args, **kwargs):
     return self.retrieve(request, *args, **kwargs)
   def put(self, request, *args, **kwargs):
     return self.update(request, *args, **kwargs)
   def delete(self, request, *args, **kwargs):
     return self.destroy(request, *args, **kwargs)

class AlbumDetails(mixins.CreateModelMixin, 
                  mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                  mixins.DestroyModelMixin, generics.GenericAPIView):
   queryset = Albums.objects.all()
   serializer_class = AlbumSerializer
   def post(self, request, *args, **kwargs):
     return self.create(request, *args, **kwargs)
   def get(self, request, *args, **kwargs):
     return self.retrieve(request, *args, **kwargs)
   def put(self, request, *args, **kwargs):
     return self.update(request, *args, **kwargs)
   def delete(self, request, *args, **kwargs):
     return self.destroy(request, *args, **kwargs)
   
class SpecDetails(mixins.CreateModelMixin, 
                  mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                  mixins.DestroyModelMixin, generics.GenericAPIView):
   queryset = Specs.objects.all()
   serializer_class = SpecsSerializer
   def post(self, request, *args, **kwargs):
     return self.create(request, *args, **kwargs)
   def get(self, request, *args, **kwargs):
     return self.retrieve(request, *args, **kwargs)
   def put(self, request, *args, **kwargs):
     return self.update(request, *args, **kwargs)
   def delete(self, request, *args, **kwargs):
     return self.destroy(request, *args, **kwargs)
# @api_view(['GET'])  
# def gene_list(request):
#   try:
#     gene = Gene.objects.all()
#   except Gene.DoesNotExist:
#       return HttpResponse(status=404) 
#   if request.method == 'GET':
#      serializer = GeneListSerializer(gene, many=True)
#      return Response(serializer.data)

class SongList(generics.ListAPIView):
   queryset = Songs.objects.filter(track_popularity__lte=10)
   serializer_class = SongListSerializer

class AlbumList(generics.ListAPIView):
   queryset = Albums.objects.filter(release__gte='1990-01-01')
   serializer_class = AlbumListSerializer

class SpecList(generics.ListAPIView):
   queryset = Specs.objects.filter(key='G')
   serializer_class = SpecListSerializer