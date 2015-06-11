#Embedded file name: /Users/jkh/Virtualenvs/Scraper/ScraperWorkspace/DjangoProject/TheIngredientSite/models.py
from django.db import models

class Recipe(models.Model):
    recipe = models.TextField()
    url = models.URLField(default='www.theingredientsite.com')

    def __str__(self):
        return self.recipe.encode('ascii', errors='replace')


class Ingredient(models.Model):
    ingredient_name = models.TextField()
    recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.ingredient_name.encode('ascii', errors='replace')


class Associative_tag(models.Model):
    association = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.association.encode('ascii', errors='replace')
