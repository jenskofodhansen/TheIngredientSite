#Embedded file name: /Users/jkh/Virtualenvs/Scraper/ScraperWorkspace/DjangoProject/DjangoProject/urls.py
from django.conf.urls import patterns, include, url
from django.contrib import admin
urlpatterns = patterns('', url('^admin/', include(admin.site.urls)), url('^', include('TheIngredientSite.urls', namespace='TheIngredientSite')))
