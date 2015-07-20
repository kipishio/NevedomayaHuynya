# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KatalogCvetov', '0013_auto_20150710_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvetikatalog',
            name='photopreview',
            field=models.ImageField(default=1, upload_to=b'preview/preview'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='photo',
            field=models.ImageField(upload_to=b'preview/cveti'),
        ),
    ]
