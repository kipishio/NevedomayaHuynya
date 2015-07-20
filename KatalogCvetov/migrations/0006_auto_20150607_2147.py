# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KatalogCvetov', '0005_auto_20150607_1525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cvetikatalog',
            old_name='sposob_razmnogeniya_cvetka',
            new_name='sposob_razmnogeniya',
        ),
    ]
