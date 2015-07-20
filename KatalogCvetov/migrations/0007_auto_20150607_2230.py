# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KatalogCvetov', '0006_auto_20150607_2147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cvetikatalog',
            old_name='name',
            new_name='name_rosteniya',
        ),
    ]
