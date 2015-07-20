# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CvetiKatalog',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Название цветка', max_length=200)),
                ('cena', models.IntegerField(verbose_name='Цена', default=0)),
                ('opisanie', models.TextField(verbose_name='Описание')),
                ('coderjat', models.TextField(verbose_name='Содержание ростения')),
                ('polza', models.CharField(verbose_name='Польза ростения', max_length=400)),
                ('sposob_razmnogeniya_cvetka', models.CharField(verbose_name='Способ размножения', max_length=200)),
                ('peresadka', models.CharField(verbose_name='Пересадка', max_length=200)),
                ('osobennosty_uhod', models.CharField(verbose_name='Особенности ухода', max_length=200)),
                ('temperatera', models.CharField(verbose_name='Температура', max_length=200)),
                ('svet', models.CharField(verbose_name='Свет', max_length=200)),
                ('poliv', models.CharField(verbose_name='Полив', max_length=200)),
                ('vlajnost_vozduha', models.CharField(verbose_name='Влажность воздуха', max_length=200)),
                ('pochva', models.CharField(verbose_name='Почва', max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KommentariyCvetka',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('kommentariy', models.CharField(verbose_name='Комментарий', max_length=200)),
                ('CvetiKatalog', models.ForeignKey(to='KatalogCvetov.CvetiKatalog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReytiтgCvetka',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('reyting', models.IntegerField(verbose_name='Рейтинг', default=0)),
                ('cveti_katalog', models.OneToOneField(to='KatalogCvetov.CvetiKatalog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
