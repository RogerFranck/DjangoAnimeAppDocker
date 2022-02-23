from .models import *
from rest_framework import serializers


class AnimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Anime  # Modelo a sacar
        fields = ['id', 'name', 'description', 'ranking', 'category',
                  'releaseDate', 'studio', 'sountrack']  # Campos a recuperar

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        return {
            'id': ret['id'],
            'name': ret['name'],
            'description': ret['description'],
            'ranking': ret['ranking'],
            'category_id': ret['category'],
        }


class AnimeCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = AnimeCategory  # Modelo a sacar
        fields = ['id', 'name']  # Campos a recuperar


class SountrackAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sountrack  # Modelo a sacar
        fields = ['id', 'name', 'duration']  # Campos a recuperar


class StudioAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio  # Modelo a sacar
        fields = ['id', 'name', 'numberOfEmployees',
                  'description']  # Campos a recuperar

class CharactersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characters  # Modelo a sacar
        fields = ['id', 'name', 'lastName']  # Campos a recuperar
