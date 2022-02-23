from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Anime', views.AnimeViewSet)
router.register(r'AnimeCatetgory', views.AnimeCategoriesViewSet)
router.register(r'Sountrack', views.SountrackAnimeViewSet)
router.register(r'Studio', views.StudioAnimeViewSet)
router.register(r'Characters', views.CharactersViewSet)

urlpatterns = [
    # path('', views.index, name='index')
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]