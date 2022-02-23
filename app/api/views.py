from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from .serializers import AnimeSerializers, AnimeCategorySerializers, SountrackAnimeSerializer, StudioAnimeSerializer, CharactersSerializer
from .models import *

# Create your views here.

def index(request):
    return HttpResponse("Hello world! A ver")


class AnimeViewSet(viewsets.ModelViewSet):
    search_fields = ['name', 'description']
    filter_backends = (filters.SearchFilter,)
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializers

class AnimeCategoriesViewSet(viewsets.ModelViewSet):
    queryset = AnimeCategory.objects.all()
    serializer_class = AnimeCategorySerializers

class SountrackAnimeViewSet(viewsets.ModelViewSet):
    queryset = Sountrack.objects.all()
    serializer_class = SountrackAnimeSerializer

class StudioAnimeViewSet(viewsets.ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioAnimeSerializer

class CharactersViewSet(viewsets.ModelViewSet):
    queryset = Characters.objects.all()
    serializer_class = CharactersSerializer