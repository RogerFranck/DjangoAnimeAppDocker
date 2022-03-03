from unicodedata import category
from venv import create
from .models import *
from rest_framework import serializers


class AnimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Anime  # Modelo a sacar
        fields = ['id', 'name', 'description', 'ranking', 'category',
                  'releaseDate', 'studio', 'sountrack']  # Campos a recuperar

        def create(self, validated_data):
            category = Anime.objects.create(**validated_data)
            return category


class AnimeCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = AnimeCategory  # Modelo a sacar
        fields = ['id', 'name']  # Campos a recuperar

        def create(self, validated_data):
            category = AnimeCategory.objects.create(**validated_data)
            return category

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.save()
            return instance


class SountrackAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sountrack  # Modelo a sacar
        fields = ['id', 'name', 'duration']  # Campos a recuperar

        def create(self, validated_data):
            category = Sountrack.objects.create(**validated_data)
            return category


class StudioAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio  # Modelo a sacar
        fields = ['id', 'name', 'numberOfEmployees',
                  'description']  # Campos a recuperar

        def create(self, validated_data):
            category = Studio.objects.create(**validated_data)
            return category


class CharactersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characters  # Modelo a sacar
        fields = ['id', 'name', 'lastName']  # Campos a recuperar

    def create(self, validated_data):
        category = Characters.objects.create(**validated_data)
        return category
