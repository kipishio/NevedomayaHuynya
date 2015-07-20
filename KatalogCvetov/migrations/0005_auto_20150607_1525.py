# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KatalogCvetov', '0004_auto_20150607_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reytingcvetka',
            name='cveti_katalog',
            field=models.ForeignKey(to='KatalogCvetov.CvetiKatalog'),
            preserve_default=True,
        ),
    ]
