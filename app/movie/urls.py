from django.urls import path, include
from rest_framework.routers import DefaultRouter

from movie import views

router = DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('actors', views.ActorViewSet)
router.register('movies', views.MovieViewSet)


app_name = 'movie'

urlpatterns = [
    path('', include(router.urls))
]
