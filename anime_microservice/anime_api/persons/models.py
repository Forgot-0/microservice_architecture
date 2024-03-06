from django.db import models
from animes.models import Anime



def person_image_path(instance, filename):
    return f'persons/{instance.anime}/{instance.title}/{filename}'


# Create your models here.
class Person(models.Model):
    title = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25, unique=True)

    description = models.TextField()

    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    gender = models.CharField(max_length=1, blank=True)
    height = models.PositiveSmallIntegerField(default=0, blank=True)
    weight = models.FloatField(default=0, blank=True)
    dead = models.BooleanField(default=True, blank=True)
    old = models.PositiveIntegerField(default=0, blank=True)

    avatar = models.ImageField(upload_to=person_image_path, blank=True)

    def __str__(self) -> str:
        return f'{self.title}'
