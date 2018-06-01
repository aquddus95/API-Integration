# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Question, Food_Place_ID_Yelp, Food_Place_ID_Zomato, Recipe, User_Detail,User_search


admin.site.register(Question)
admin.site.register(Food_Place_ID_Yelp)
admin.site.register(Food_Place_ID_Zomato)
admin.site.register(Recipe)
admin.site.register(User_Detail)
admin.site.register(User_search)