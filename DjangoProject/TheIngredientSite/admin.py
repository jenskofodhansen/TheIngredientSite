#Embedded file name: /Users/jkh/Virtualenvs/Scraper/ScraperWorkspace/DjangoProject/TheIngredientSite/admin.py
from django.contrib import admin
from TheIngredientSite.models import Ingredient, Recipe, Associative_tag
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Associative_tag)
