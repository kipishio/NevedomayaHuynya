# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KatalogCvetov', '0002_auto_20150607_0247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cvetikatalog',
            old_name='name_cver',
            new_name='name',
        ),
    ]
