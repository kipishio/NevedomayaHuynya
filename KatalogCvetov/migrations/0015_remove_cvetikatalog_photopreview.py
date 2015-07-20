# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KatalogCvetov', '0014_auto_20150710_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cvetikatalog',
            name='photopreview',
        ),
    ]
