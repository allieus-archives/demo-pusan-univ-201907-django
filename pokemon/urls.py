from django.urls import path

from pokemon.views import index, pokemon_new, pokemon_edit

urlpatterns = [
    path('', index),
    # path('pokemon_list.html', pokemon_list_html),
    path('new/', pokemon_new),
    path('<int:pk>/edit/', pokemon_edit),
    # re_path(r'(?P<pk>\d+)', pokemon_edit),
]
