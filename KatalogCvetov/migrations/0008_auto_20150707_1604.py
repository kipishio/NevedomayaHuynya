# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KatalogCvetov', '0007_auto_20150607_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kommentariycvetka',
            name='kommentariy',
            field=models.CharField(max_length=200, verbose_name='Комментарий ростения'),
            preserve_default=True,
        ),
    ]
