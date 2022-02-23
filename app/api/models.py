from django.db import models

class Studio(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    numberOfEmployees = models.IntegerField(3)

class Sountrack(models.Model):
    name = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)

class AnimeCategory(models.Model):
    name = models.CharField(max_length=250)

    
class Characters(models.Model):
    name = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)

class Anime(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    ranking = models.IntegerField(1)
    category = models.ManyToManyField(AnimeCategory)
    releaseDate = models.CharField(max_length=250)
    studio = models.ManyToManyField(Studio)
    sountrack = models.ManyToManyField(Sountrack)
    characters = models.ManyToManyField(Characters)


# Cambiar nombres sin "Anime"
# ManyToMany en todo
# Caracteres ManytoMany
# Enviar copia de sql
