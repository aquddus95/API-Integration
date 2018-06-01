import os
from django.core.wsgi import get_wsgi_application
import requests
import json

## Allows for Script to Load Django Models 
os.environ['DJANGO_SETTINGS_MODULE'] = 'finalproject.settings'
application = get_wsgi_application()
from polls.models import Recipe



## OAuth Needed to access the API 
## Currently the Key is not Valid anymore since this project went public 

header = {
'X-Mashape-Key': 'KRdNRE1KYOmshIGsBJZFy7agyQmSp1N1Nq8jsnscl7kC3xEGFY'
}
url='https://webknox-recipes.p.mashape.com/recipes/search?cuisine=Italian'
response = requests.get(url, headers=header)
food_recipes=response.json()
food_recipes=food_recipes['results']
print(food_recipes)
idx=0
for i in food_recipes:
    food_recipe=food_recipes[idx]
    recipe_id=food_recipe['id']
    title=food_recipe['title']
    readyInMinutes=food_recipe['readyInMinutes']
    entry=Recipe(recipe_id= recipe_id, cusine= 'Italian', title=title,readyInMinutes=readyInMinutes)
    entry.save()
    idx+=1




