# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KatalogCvetov', '0003_auto_20150607_0251'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReytingCvetka',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('reyting', models.IntegerField(verbose_name='Рейтинг', default=0)),
                ('cveti_katalog', models.OneToOneField(to='KatalogCvetov.CvetiKatalog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='reytiтgcvetka',
            name='cveti_katalog',
        ),
        migrations.DeleteModel(
            name='ReytiтgCvetka',
        ),
    ]
