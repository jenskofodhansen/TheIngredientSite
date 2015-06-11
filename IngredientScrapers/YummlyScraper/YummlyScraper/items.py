#Embedded file name: /Users/jkh/Virtualenvs/Scraper/ScraperWorkspace/IngredientScrapers/YummlyScraper/YummlyScraper/items.py
import scrapy
from scrapy.contrib.djangoitem import DjangoItem
from TheIngredientSite.models import Recipe

class YummlyRecipeItem(DjangoItem):
    django_model = Recipe
