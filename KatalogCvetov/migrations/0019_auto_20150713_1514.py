# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('KatalogCvetov', '0018_auto_20150713_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoView',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='preview/cveti', blank=True)),
                ('CvetiKatalog', models.ForeignKey(to='KatalogCvetov.CvetiKatalog', verbose_name='Каталог цветов')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='cvetikatalog_foto',
            name='CvetiKatalog',
        ),
        migrations.DeleteModel(
            name='CvetiKatalog_foto',
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 15, 14, 45, 936929), blank=True, verbose_name='Дата публикации'),
            preserve_default=True,
        ),
    ]
