from django.db import models
# Create your models here.

def anime_avatar_path(instance, filename):
    return f'animes/{instance.slug}/{filename}'


class Anime(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    description = models.TextField()
    image = models.ImageField(blank=True)

    views = models.IntegerField(default=0)

    genres = models.ManyToManyField('Tag', related_name='genre')
    topics = models.ManyToManyField('Tag', related_name='topic')

    years = models.ManyToManyField('Year')

    avatar = models.ImageField(upload_to=anime_avatar_path, blank=True)

    def __str__(self) -> str:
        return self.slug
    

class Season(models.Model):
    title = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40, unique=True)
    anime = models.ForeignKey('Anime', on_delete=models.CASCADE, related_name='seasons')

    def __str__(self) -> str:
        return self.slug


class Episode(models.Model):
    title = models.CharField(max_length=20)
    season = models.ForeignKey('Season', on_delete=models.CASCADE, related_name='episodes')

    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    slug = models.SlugField(unique=True, primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name
    

class Year(models.Model):
    slug = models.SlugField(unique=True, primary_key=True)
    name = models.PositiveSmallIntegerField(default=0)

    def __str__(self) -> str:
        return str(self.name)