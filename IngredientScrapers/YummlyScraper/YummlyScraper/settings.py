#Embedded file name: /Users/jkh/Virtualenvs/Scraper/ScraperWorkspace/IngredientScrapers/YummlyScraper/YummlyScraper/settings.py
import sys
sys.path.append('/Users/jkh/Virtualenvs/Scraper/ScraperWorkspace/DjangoProject')
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoProject.settings'
BOT_NAME = 'YummlyScraper'
SPIDER_MODULES = ['YummlyScraper.spiders']
NEWSPIDER_MODULE = 'YummlyScraper.spiders'
