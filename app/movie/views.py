from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from moviestore.models import Category, Actor

from movie import serializers


class CategoryViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage categories in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ActorViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage actors in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = serializers.ActorSerializer
