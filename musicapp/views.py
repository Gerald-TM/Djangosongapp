from django.shortcuts import render
from .models import Song, Artiste
from rest_framework import generics
from .serializers import SongSerializer, ArtisteSerializer

# Create your views here.
# views for your Song
class SongList(generics.ListCreateAPIView):
    queryset =  Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

# views for your Artiste
class ArtisteList(generics.ListCreateAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class ArtisteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer