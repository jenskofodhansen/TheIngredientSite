from django.contrib import admin
from TheIngredientSite.models import Ingredient, Recipe, Associative_tag

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Associative_tag)