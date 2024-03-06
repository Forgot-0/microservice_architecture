from rest_framework import serializers
from persons.models import Person
from animes.models import Anime
from typing import TypedDict
from animes.api_v1.serializers import AnimeSerializer



class PersonSerializer(serializers.ModelSerializer):
    anime = AnimeSerializer()
    anime_pk = serializers.PrimaryKeyRelatedField(queryset=Anime.objects.all(), source='anime', write_only=True)

    class Meta:
        model = Person
        fields = (
            'title',
            'slug',
            'description',
            'anime',
            'anime_pk',    
            'gender', 
            'height', 
            'weight',
            'dead', 
            'old'
            )


class PersonSchema(TypedDict):
    title: str
    slug: str
    avatar: str


class PersonDetailSerializer(serializers.ModelSerializer):
    persons = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = (
            'title',
            'slug',
            'description',
            'anime',
            'persons',
            'gender', 
            'height', 
            'weight', 
            'dead', 
            'old'
            )
        depth = 1

    def get_persons(self, obj) -> PersonSchema:
        return Person.objects.all().exclude(pk=obj.pk).values('title', 'slug', 'avatar')