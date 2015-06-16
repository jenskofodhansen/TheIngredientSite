# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TheIngredientSite', '0002_ingredient_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recipe', models.TextField()),
                ('url', models.URLField(default=b'www.theingredientsite.com')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='ingredient',
            new_name='ingredient_name',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='url',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipes',
            field=models.ManyToManyField(to='TheIngredientSite.Recipe'),
            preserve_default=True,
        ),
    ]
