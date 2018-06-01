# -*- coding: utf-8 -*-
#the following code below repersents the schema for the web application

import datetime

from django.db import models
from django.utils import timezone

#the following database component holds the question table
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text


#the following table holds the restaraunt and its info from yelp
class Food_Place_ID_Yelp(models.Model):
	restaraunt_id=models.CharField(max_length=256, primary_key=True)
	name=models.CharField(max_length=256, null=True)
	category=models.CharField(max_length=256)
	phone_num=models.CharField(max_length=256)
	rating=models.IntegerField()
	image_url=models.CharField(max_length=256)
	city=models.CharField(max_length=256)
	country=models.CharField(max_length=256)
	state=models.CharField(max_length=256)
	address=models.CharField(max_length=256)
	zip_code=models.CharField(max_length=256)
	def __str__(self):
		return self.name

	


#the following holds restaraunt info from zomato api
class Food_Place_ID_Zomato(models.Model):
	restaraunt_id=models.CharField(max_length=256, primary_key=True)
	city=models.CharField(max_length=256)
	address=models.CharField(max_length=256)
	name=models.CharField(max_length=256, null=True)
	cusine=models.CharField(max_length=256)
	menu_url=models.CharField(max_length=256)
	average_cost_for_two=models.CharField(max_length=256)
	def __str__(self):
		return self.name


#the following holds recipe basic info
class Recipe(models.Model):
	recipe_id=models.IntegerField()
	cusine=models.CharField(max_length=256, null=True)
	title=models.CharField(max_length=256)
	readyInMinutes=models.IntegerField()
	def __unicode__(self):
		return self.title





#the following two tables hold info related to the user
class User_Detail(models.Model):
	user_ID=models.CharField(max_length=256)
	user_name=models.CharField(max_length=256)


class User_search(models.Model):
	user_info=models.ForeignKey(User_Detail,on_delete=models.CASCADE)
	user_query=models.CharField(max_length=256)
	user_selected_food_place=models.CharField(max_length=256)











