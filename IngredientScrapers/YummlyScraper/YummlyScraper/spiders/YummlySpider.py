#Embedded file name: /Users/jkh/Virtualenvs/Scraper/ScraperWorkspace/IngredientScrapers/YummlyScraper/YummlyScraper/spiders/YummlySpider.py
"""
Created on Feb 28, 2015

@author: jkh
"""
from YummlyScraper.items import YummlyRecipeItem
from TheIngredientSite.models import Ingredient
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from BeautifulSoup import BeautifulSoup
import django

class YummlySpider(CrawlSpider):
    name = 'YummlyScraper'
    start_urls = ['http://www.yummly.com/recipes/chilli-garlic', 'http://www.yummly.com/recipes/healthy-macaroni-and-cheese-with-spinach', 'http://www.yummly.com/recipes/bhindi-masala']
    allowed_domains = ['yummly.com']
    rules = (Rule(LinkExtractor(allow=('recipe.+-\\d{1,6}',), deny='login'), callback='parse_item', follow=False), Rule(LinkExtractor(allow='recipe')))

    def parse_item(self, response):
        soup = BeautifulSoup(response.body)
        recipe = soup.find('h1', {'itemprop': 'name'})
        self.log(recipe)
        if recipe is not None:
            recipeName = recipe.get('title').lower()
            self.log('Got recipe %s at %s' % (recipeName, response.url))
            django.setup()
            recipeItem, created = YummlyRecipeItem.django_model.objects.get_or_create(recipe=recipeName)
            if created is not True:
                return
            recipeItem.name = recipeName
            recipeItem.url = response.url
            ingredients = soup.findAll('strong', {'class': 'name'})
            for yummlyIngredient in ingredients:
                yummly_ingredient_name = yummlyIngredient.text.lower()
                ingredientItem, created = Ingredient.objects.get_or_create(ingredient_name=yummly_ingredient_name)
                if created is True:
                    ingredientItem.ingredient_name = yummly_ingredient_name
                    ingredientItem.save()
                recipeItem.ingredient_set.add(ingredientItem)

            recipeItem.save()
