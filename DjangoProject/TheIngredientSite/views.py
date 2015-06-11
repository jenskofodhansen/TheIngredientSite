#Embedded file name: /Users/jkh/Virtualenvs/Scraper/ScraperWorkspace/DjangoProject/TheIngredientSite/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from TheIngredientSite.models import Ingredient, Recipe, Associative_tag
from django.db.models import Count
import json
import wikipedia

def index(request):
    return redirect('/ingredient_of_the_day')


def ingredient_of_the_day(request):
    ingredient_object = Ingredient.objects.get(ingredient_name='cheese')
    ingredient_name = ingredient_object.ingredient_name
    return ingredient(request, ingredient_name)


def ingredient(request, ingredient_name):
    try:
        ingredient_object = Ingredient.objects.get(ingredient_name=ingredient_name)
    except:
        return redirect('/ingredient_of_the_day')

    used_in_recipes = Recipe.objects.filter(ingredient=ingredient_object)[0:9]
    related_ingredients = Ingredient.objects.filter(recipes__in=used_in_recipes).annotate(nums=Count('ingredient_name')).order_by('nums').reverse()[1:31]
    association_tags = Associative_tag.objects.filter(ingredients=ingredient_object)
    wiki_image_urls = {}
    bg_image = ''
    wiki_link = ''
    try:
        wiki_page = wikipedia.page(ingredient_name)
        wiki_summary = wiki_page.summary
        wiki_image_urls = wiki_page.images
        wiki_link = wiki_page.url
        wiki_image_urls = [ item for item in wiki_image_urls if 'jpg' in item.lower() ]
        if len(wiki_image_urls) > 0:
            bg_image = wiki_image_urls[0]
    except:
        wiki_summary = 'Could not find any information about ' + ingredient_name + ' on Wikipedia'

    context = {'ingredient_name': ingredient_name,
     'used_in_recipes': used_in_recipes,
     'related_ingredients': related_ingredients,
     'association_tags': association_tags,
     'wiki_summary': wiki_summary,
     'wiki_image_urls': wiki_image_urls,
     'wiki_link': wiki_link,
     'bg_image': bg_image}
    return render(request, 'TheIngredientSite/index.html', context)


def get_ingredients(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        ingredients = Ingredient.objects.filter(ingredient_name__icontains=q)[:20]
        results = []
        for ingredient in ingredients:
            ingredient_json = {}
            ingredient_json['id'] = ingredient.id
            ingredient_json['label'] = ingredient.ingredient_name
            ingredient_json['value'] = ingredient.ingredient_name
            results.append(ingredient_json)

        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def set_association(request):
    print 'set associations'
    if request.is_ajax():
        ingredient_to_update = request.GET.get('ingredient', '')
        tag = request.GET.get('tag', '').lower()
        ingredient_item = Ingredient.objects.get(ingredient_name=ingredient_to_update)
        if ingredient_item is not None:
            new_tag, created = Associative_tag.objects.get_or_create(association=tag)
            new_tag.ingredients.add(ingredient_item)
            new_tag.save()
            data = 'success'
        else:
            data = 'fail'
    else:
        data = 'fail'
    return_json = json.dumps(data)
    mimetype = 'application/json'
    return HttpResponse(return_json, mimetype)
