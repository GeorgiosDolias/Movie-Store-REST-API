from rest_framework import serializers

from moviestore.models import Category, Actor, Movie


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category objects"""

    class Meta:
        model = Category
        fields = ('id', 'name')
        read_only_fields = ('id',)


class ActorSerializer(serializers.ModelSerializer):
    """Serializer for actor objects"""

    class Meta:
        model = Actor
        fields = ('id', 'name')
        read_only_fields = ('id',)


class MovieSerializer(serializers.ModelSerializer):
    """Serializer for movie objects"""
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        many=True
    )
    categories = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True
    )

    class Meta:
        model = Movie
        fields = ('id', 'title', 'year', 'summary', 'categories', 'actors')
        read_only_fields = ('id',)


class MovieDetailSerializer(MovieSerializer):
    """Serialize a movie detail"""
    actors = ActorSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
