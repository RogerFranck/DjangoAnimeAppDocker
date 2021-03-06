# Generated by Django 4.0.2 on 2022-02-23 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Characters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('lastName', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Sountrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('duration', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
                ('numberOfEmployees', models.IntegerField(verbose_name=3)),
            ],
        ),
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
                ('ranking', models.IntegerField(verbose_name=1)),
                ('releaseDate', models.CharField(max_length=250)),
                ('category', models.ManyToManyField(to='api.AnimeCategory')),
                ('characters', models.ManyToManyField(to='api.Characters')),
                ('sountrack', models.ManyToManyField(to='api.Sountrack')),
                ('studio', models.ManyToManyField(to='api.Studio')),
            ],
        ),
    ]
