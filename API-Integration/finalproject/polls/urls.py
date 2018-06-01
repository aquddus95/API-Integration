from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'find_restaurants', views.find_restaurants, name='find_restaurants'),
    url(r'restaurants_results', views.restaurants_results, name='restaurants_results'),
    url(r'find_recipes', views.find_recipes, name='find_recipes'),
    url(r'recipes_results', views.recipes_results, name='recipes_results')
]