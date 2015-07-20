# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KatalogCvetov', '0009_auto_20150708_1417'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VidiRosteniy',
            new_name='VidiRasteniy',
        ),
        migrations.RenameField(
            model_name='cvetikatalog',
            old_name='VidiRosteniy',
            new_name='VidiRasteniy',
        ),
    ]
