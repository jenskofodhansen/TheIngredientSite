# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TheIngredientSite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='Ingredient',
            name='url',
            field=models.URLField(default=b'www.blank.com'),
            preserve_default=True,
        ),
    ]
