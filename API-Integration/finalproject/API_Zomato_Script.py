import os
from django.core.wsgi import get_wsgi_application
import requests
import json

## Loading Django settings to get the script access to Django Models (tables/schema)
os.environ['DJANGO_SETTINGS_MODULE'] = 'finalproject.settings'
application = get_wsgi_application()
from polls.models import Food_Place_ID_Zomato


## Adding OAuth token information to access Zomato API
header = {
"User-agent": "curl/7.43.0",
'X-Zomato-API-Key': '4903b587901a5352f403a3a97da3543a'
}

## Note have to lookup entity ID on Zomoato's online API documentation for a specific location from which you are trying to pull restaurant information for 
url='https://developers.zomato.com/api/v2.1/search?entity_id=685&entity_type=city&count=100'
response = requests.get(url, headers=header)
food_places=response.json()
food_places=food_places['restaurants']
idx=0


## Parsing Zomato API response
for i in food_places:
    food_place=food_places[idx]
    restaraunt_id=food_place['restaurant']['id']
    city=food_place['restaurant']['location']['city']
    address=food_place['restaurant']['location']['address']
    name=food_place['restaurant']['name']
    cusine=food_place['restaurant']['cuisines']
    menu=food_place['restaurant']['menu_url']
    cost=food_place['restaurant']['average_cost_for_two']
    entry=Food_Place_ID_Zomato(restaraunt_id= restaraunt_id,city=city,address=address,name=name,cusine=cusine,menu_url=menu,average_cost_for_two=cost)
    entry.save()
    idx+=1

