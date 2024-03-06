from rest_framework import serializers
from animes.models import Anime, Season, Episode, Tag, Year




class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'slug')


class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = ('name', 'slug')


class AnimeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    genres_pk = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), source='genres', write_only=True, many=True)
    topics_pk = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), source='topics', write_only=True, many=True)
    years_pk = serializers.PrimaryKeyRelatedField(
        queryset=Year.objects.all(), source='years', write_only=True, many=True)
    

    genres = TagSerializer(many=True, read_only=True)
    topics = TagSerializer(many=True, read_only=True)
    years = YearSerializer(many=True, read_only=True)


    class Meta:
        model = Anime
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'avatar',
            'genres',
            'genres_pk',

            'topics',
            'topics_pk',

            'years',
            'years_pk',
            )



class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = "__all__"



class SeasonSerializer(serializers.ModelSerializer):
    episodes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Season
        fields = (
            'title',
            'slug',
            'episodes'
        )


class AnimeDetailSerializer(serializers.ModelSerializer):
    seasons = SeasonSerializer(many=True, read_only=True)

    genres = TagSerializer(many=True, read_only=True)
    topics = TagSerializer(many=True, read_only=True)
    years = YearSerializer(many=True, read_only=True)
    
    class Meta:
        model = Anime
        fields = (
            'title',
            'slug',
            'description',
            'genres',
            'topics',
            'years',
            'seasons'
            )
