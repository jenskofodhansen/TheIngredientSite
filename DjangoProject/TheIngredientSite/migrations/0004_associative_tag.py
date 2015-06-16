# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TheIngredientSite', '0003_auto_20150307_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='Associative_tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('association', models.TextField()),
                ('ingredients', models.ManyToManyField(to='TheIngredientSite.Ingredient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
