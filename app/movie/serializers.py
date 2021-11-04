from rest_framework import serializers

from moviestore.models import Category, Actor


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
