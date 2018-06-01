# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.template.loader import get_template
from polls.models import Food_Place_ID_Yelp,Food_Place_ID_Zomato, Recipe, User_Detail
from django.contrib.auth.models import User

import httplib
import json
import urllib
from urllib import urlencode 
import requests

#the following setups the search page with a simple search box to get user input
## template contains an input forum for the user to type in the Restaurant Name
def find_restaurants(request):
	context= {}
	template= get_template('find_restaurants.html')
	return HttpResponse(template.render(context, request))


#the following function gets the proper restaraunt information based on what the user passed into the the input_box
def restaurants_results(request):
	both=False
	#get user input and store it into a variable
	input_box= request.GET['query']

	#check if user typed in the exact name of the restaraunt in the database
	search_results= Food_Place_ID_Yelp.objects.filter(name__startswith=input_box)
	

	lis=[]
	#name of restaurant
	name=None
	#image of restaurant pulled from Yelp API
	image=None
	# Category type of the Restaurant according to Yelp
	category=None
	# Restaurant Rating
	rating=None
	# phone number of the restaurant
	phone_num=None
	# address of the restaurant
	address=None
	# zipcode of the restaurant
	zip_code=None

	

	# Cuisine information which is pulled from zomato api
	cusine=None
	# menu url that link to zomoato's url page for the particular restaurant that will have access to the restaurant's url if available
	menu_url=None
	average_cost_for_two=None
	# variable contains the link for which the user clicks on to get the reccomended recipes based of the restaurant
	recipe=None

	#If condition checks to see if the user input was an exact name of a restaurant in the database
	if(search_results):
		#user typed in the exact restaurant name and now have to do an api call to yelp for reviews (limit 3)
		# since we have stored the restuarants id we can make another call to Yelp api to get reviews for this restaurant from yelp's api


		#Loading variable that were initalized above with the proper information from the database
		search_results1=search_results[0].restaraunt_id
		name=search_results[0].name
		image=search_results[0].image_url
		category=search_results[0].category
		rating=search_results[0].rating  
		phone_num=search_results[0].phone_num
		address=search_results[0].address  
		zip_code=search_results[0].zip_code

		#food place contains the restaurants Id which is used in the Yelp API call
		food_place_name=search_results1
		headers = 	{
					'authorization': "Bearer 1_-tP4IlMNVpRBOj68A5aZJ4FwHdMGCps6xN9PFV0q1AmreUfNclD1Hw0bqQuCSfjthDFl4JQGtfTmvI321ffJ6LcPZ0O2XDYfa5OedFipN4Riw7iibTBCvUR6fVWnYx",
					'cache-control': "no-cache", 
					}

		make_connection = httplib.HTTPSConnection("api.yelp.com")
		res_id= food_place_name
		make_connection.request("GET", "https://api.yelp.com/v3/businesses/"+res_id+"/reviews", headers=headers)
		result = make_connection.getresponse()
		json_data = result.read()
		json_data = json.loads(json_data.decode("utf-8"))
		reviews=json_data['reviews']
		for review in reviews:
			lis.append(review['user']['name'] + ':'+ ' '+ (review['text']))



		#check if the restaurant name is in the zomato databse	
		search_results= Food_Place_ID_Zomato.objects.filter(name__startswith=input_box)
		if(search_results):
			both=True
			#restaurant is in the zomato databse so setup the api call for getting reviews for this restaurant from zomato as well  (limit 5)
			search_results1=search_results[0].restaraunt_id
			cusine=search_results[0].cusine

			entry=User_Detail(user_ID= str(request.user.username), user_name= cusine)
			entry.save()

			recipe="http://127.0.0.1:8000/database/recipes_results?query=" + str(cusine)
			menu_url=search_results[0].menu_url
			average_cost_for_two=search_results[0].average_cost_for_two

			header = 	{
						"User-agent": "curl/7.43.0",
						'X-Zomato-API-Key': '4903b587901a5352f403a3a97da3543a'
						}
			url='https://developers.zomato.com/api/v2.1/reviews?res_id='
			res_id=str(search_results1)
			url=url+res_id
			response = requests.get(url, headers=header)
			reviews=response.json()

			## parse Zomoato API response and collect all reviews in a list
			reviews=reviews['user_reviews']
			for review in reviews:
				lis.append(review['review']['user']['name']+ ': '+ review['review']['review_text'])

	#if user did not type in the exact name of the restaurant then check if the user entered a city name and if so return all restaurants with the user input city name
	elif(Food_Place_ID_Yelp.objects.filter(city=input_box)):
		lis=[]
		lis.append(" You Search Results for the given City: ")
		food_places=Food_Place_ID_Yelp.objects.filter(city=input_box)
		for place in food_places:
			lis.append(place.name+' Type: '+place.category+' Rating: '+str(place.rating)+ ' Number: ' + place.phone_num)

	# if user did not type in exact name or city name check if the user entered a zip code and if so find all restaurants with the specified zip code
	elif(Food_Place_ID_Yelp.objects.filter(zip_code=input_box)):
		lis=[]
		lis.append(" You Search Results for the given Zip Code: ")
		food_places=Food_Place_ID_Yelp.objects.filter(zip_code=input_box)
		for place in food_places:
			lis.append(place.name+' Type: '+place.category+' Rating: '+str(place.rating)+ ' Number: ' + place.phone_num)

	#if restaurant that was searched for was not in both Yelp and Zomato tables then use a generic template which presents a list of names of the restaurants related to user search query
	if(both == False):
		template= get_template('restaurants_results.html')
	else:
		template= get_template('restaurants_both_results.html')
	context={'search_results':lis, 'name':name, 'image':image, 'category':category, 'rating':rating, 'phone_num':phone_num, 'address':address, 'zip_code':zip_code, 'cusine':cusine, 'menu_url':menu_url, 'average_cost_for_two':average_cost_for_two, 'recipe':recipe }
	return HttpResponse(template.render(context,request))

#setup simple search function for recipes
def find_recipes(request):
	context= {}
	template= get_template('find_recipes.html')
	return HttpResponse(template.render(context, request))

	
#find recipes either based on title or cusine based of the userinput given from the search recipe page
def recipes_results(request):
	template= get_template('recipes_results.html')
	input_box= request.GET['query']
	search_results= Recipe.objects.filter(title=input_box)
	lis=[]

	## a special search query which is activated if the user clicks on the reccomendation button on the homepage
	if(input_box == 'user'):
		##check user search history
		search_results=User_Detail.objects.filter(user_ID= request.user.username)
		index=len(search_results)
		search=search_results[index-1].user_name
		search=search[1:5]
		## find recipes based of what the user recently searched
		search_results=Recipe.objects.filter(cusine__icontains=search)
		for search_result in search_results:
			lis.append(' Cuisine: '+ search_result.cusine +' recipe title: '+ search_result.title + ' recipe ready time: ' + str(search_result.readyInMinutes) )	

		food_places=Food_Place_ID_Zomato.objects.filter(cusine__icontains=search)
		for place in food_places:
			lis.append(place.name+' Type: '+place.cusine+' Address: '+str(place.address)+ ' City: ' + place.city)	

			
	elif(search_results):
		lis.append("General Information ")
		lis.append(' Cuisine: '+ search_results[0].cusine +' recipe title: '+ search_results[0].title + ' recipe ready time: ' + str(search_results[0].readyInMinutes) )

	elif(True):
		check_cusine=input_box[1:5]
		search_results=Recipe.objects.filter(cusine__icontains=check_cusine)
		for search_result in search_results:
			lis.append('recipe id: '+ str(search_result.recipe_id) + ' Cuisine: '+ search_result.cusine +' recipe title: '+ search_result.title + ' recipe ready time: ' + str(search_result.readyInMinutes) )	

	
	elif(Recipe.objects.filter(cusine=input_box)):
		lis=[]
		lis.append("General Information ")
		search_results=Recipe.objects.filter(cusine=input_box)
		for search_result in search_results:
			lis.append('recipe id: '+ str(search_result.recipe_id) + ' Cuisine: '+ search_result.cusine +' recipe title: '+ search_result.title + ' recipe ready time: ' + str(search_result.readyInMinutes) )


	context= { 'search_results':lis}
	return HttpResponse(template.render(context,request))


  
