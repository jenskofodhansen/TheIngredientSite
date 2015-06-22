from django.conf.urls import patterns, url

from TheIngredientSite import views

urlpatterns = patterns('',
    url(r'^api/get_ingredients$', views.get_ingredients, name='get_ingredients'),
    url(r'^api/set_association$', views.set_association, name='set_associations'),
    url(r'^ingredient/(?P<ingredient_name>.+)$', views.ingredient, name='ingredient'),
    url(r'^ingredient_of_the_day$', views.ingredient_of_the_day, name='ingredient_of_the_day'),
    url('^$', views.index, name='index')
)
