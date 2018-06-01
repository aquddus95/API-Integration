# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from polls.models import Food_Place_ID_Yelp,Food_Place_ID_Zomato, Recipe, Recipe_Detail

class YelpTestCase(TestCase):
    def setUp(self):
        Food_Place_ID_Yelp.objects.create(restaraunt_id=1, name= "something",category= "food1",phone_num="some number",rating=2,image_url="None",city="Sycamore",country="USA",state="IL",address="hi",zip_code="123")
        Food_Place_ID_Yelp.objects.create(restaraunt_id=2, name="something2", category= "food2",phone_num="some number",rating=2,image_url="None",city="Sycamore",country="USA",state="IL",address="hi",zip_code="123")

    def test_yelp(self):

        foodplace1 = Food_Place_ID_Yelp.objects.get(restaraunt_id=1, name= "something",category= "food1",phone_num="some number",rating=2,image_url="None",city="Sycamore",country="USA",state="IL",address="hi",zip_code="123")
        foodplace2 = Food_Place_ID_Yelp.objects.get(restaraunt_id=2, name="something2", category= "food2",phone_num="some number",rating=2,image_url="None",city="Sycamore",country="USA",state="IL",address="hi",zip_code="123")


class ZomatoTestCase(TestCase):
    def setUp(self):
        Food_Place_ID_Zomato.objects.create(restaraunt_id=1, name= "something",cusine= "food1",average_cost_for_two="some number",city="Sycamore",address="hi",menu_url= "none")

    def test_zomato(self):

        foodplace1 = Food_Place_ID_Zomato.objects.get(restaraunt_id=1, name= "something",cusine= "food1",average_cost_for_two="some number",city="Sycamore",address="hi", menu_url= "none")


class RecipeTestCase(TestCase):
    def setUp(self):
        Recipe.objects.create(recipe_id= 1, title= "good", readyInMinutes=30)

    def test_recipe(self):

        foodrecipe1 = Recipe.objects.get(recipe_id= 1, title= "good", readyInMinutes=30)


class Recipe_Detail_TestCase(TestCase):
    def setUp(self):
    	Recipe.objects.create(recipe_id= 1, title= "good", readyInMinutes=30)
    	foodrecipe1 = Recipe.objects.get(recipe_id= 1, title= "good", readyInMinutes=30)
        Recipe_Detail.objects.create(recipe_detail_id=foodrecipe1, recipe_detail_title= "good", image_url='none',ingredients='none')

    def test_detail(self):

        foodrecipe_Detail1 = Recipe_Detail.objects.get(recipe_detail_title= "good", image_url='none',ingredients='none')
        

