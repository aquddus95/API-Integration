import os
from django.core.wsgi import get_wsgi_application
import httplib
import json
import urllib
from urllib import urlencode

# Loading Django settings to allow for script to use Django Models that were created for this project
os.environ['DJANGO_SETTINGS_MODULE'] = 'finalproject.settings'
application = get_wsgi_application()
from polls.models import Food_Place_ID_Yelp



## oAuth with token needed to access Yelp's API
headers = {
'authorization': "Bearer 1_-tP4IlMNVpRBOj68A5aZJ4FwHdMGCps6xN9PFV0q1AmreUfNclD1Hw0bqQuCSfjthDFl4JQGtfTmvI321ffJ6LcPZ0O2XDYfa5OedFipN4Riw7iibTBCvUR6fVWnYx",
'cache-control': "no-cache",
}
#need the following parameters (type dict) to perform business search.
## Right now have the Yelp Script Pull Restaurants based off zip code and the current zip code is for Sycamore, IL which can be changed based off which located restaurants you want to pull from the Yelp API 
parameters = {'location':'60178',}

parameter_string = urllib.urlencode(parameters)
make_connection = httplib.HTTPSConnection("api.yelp.com")
make_connection.request("GET", "/v3/businesses/search?"+parameter_string, headers=headers)

result = make_connection.getresponse()
json_data = result.read()
json_data = json.loads(json_data.decode("utf-8"))
food_places=json_data['businesses']

idx=0

## Following parses the API response to get logistacal information regarding a restaurant
for i in food_places:
    food_place= food_places[idx]
    res_id=food_place['id'] 
    name=food_place['name'] 
    category=food_place['categories'][0]['alias']
    phone_num=food_place['phone'] 
    rating=food_place['rating'] 
    image=food_place['image_url'] 
    city=food_place['location']['city']
    country=food_place['location']['country'] 
    state=food_place['location']['state'] 
    address=food_place['location']['address1'] 
    zipcode=food_place['location']['zip_code']
    entry=Food_Place_ID_Yelp(restaraunt_id=res_id,name= name,category= category,phone_num= phone_num,rating=rating,image_url=image,city=city,country=country,state=state,address=address,zip_code=zipcode)
    entry.save()
    idx+=1