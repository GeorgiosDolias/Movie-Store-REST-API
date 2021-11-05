from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from moviestore.models import Category, Actor, Movie

from movie import serializers


class BaseMovieAttrViewSet(
                            viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):
    """Base viewset for user owned movie attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return objects for current user"""
        assigned_only = bool(self.request.query_params.get('assigned_only'))
        queryset = self.queryset
        if assigned_only:
            queryset = queryset.filter(movie__isnull=False)

        return queryset.filter().order_by('-name').distinct()

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save()


class CategoryViewSet(BaseMovieAttrViewSet):
    """Manage categories in the database"""
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ActorViewSet(BaseMovieAttrViewSet):
    """Manage actors in the database"""
    queryset = Actor.objects.all()
    serializer_class = serializers.ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """Manage movies in the database"""
    serializer_class = serializers.MovieSerializer
    queryset = Movie.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def _params_to_ints(self, qs):
        """Convert a list of string ID's to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrieve the movies for the authenticated user"""
        categories = self.request.query_params.get('categories')
        queryset = self.queryset
        if categories:
            categories_ids = self._params_to_ints(categories)
            queryset = queryset.filter(categories__id__in=categories_ids)

        return queryset

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'retrieve':
            return serializers.MovieDetailSerializer

        return self.serializer_class
