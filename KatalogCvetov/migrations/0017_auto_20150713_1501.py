# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('KatalogCvetov', '0016_auto_20150710_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvetikatalog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 15, 1, 10, 671298), verbose_name='Дата публикации', blank=True),
            preserve_default=True,
        ),
    ]
