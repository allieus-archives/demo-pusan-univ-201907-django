from django.urls import path, include

from pokemon.views import index, pokemon_new, pokemon_edit

urlpatterns = [
    path('', index),
    # path('pokemon_list.html', pokemon_list_html),
    path('new/', pokemon_new),
    path('<int:pk>/edit/', pokemon_edit),
    # re_path(r'(?P<pk>\d+)', pokemon_edit),
]

from rest_framework.routers import DefaultRouter
from .views import PokemonViewSet

router = DefaultRouter()
router.register('pokemons', PokemonViewSet)

urlpatterns += [
    path('api/v1/', include(router.urls)),
]
