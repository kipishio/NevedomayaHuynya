# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('KatalogCvetov', '0015_remove_cvetikatalog_photopreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='CvetiKatalog_foto',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('photo', models.ImageField(blank=True, upload_to='preview/cveti')),
                ('CvetiKatalog', models.ForeignKey(verbose_name='Каталог цветов', to='KatalogCvetov.CvetiKatalog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='VidiRasteniy',
            field=models.ForeignKey(verbose_name='Виды растений', to='KatalogCvetov.VidiRasteniy'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='cena',
            field=models.IntegerField(default=0, blank=True, verbose_name='Цена'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='coderjat',
            field=models.TextField(blank=True, verbose_name='Содержание ростения'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='name_rosteniya',
            field=models.CharField(max_length=200, verbose_name='Название цветка'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='opisanie',
            field=models.TextField(blank=True, verbose_name='Описание'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='osobennosty_uhod',
            field=models.CharField(blank=True, max_length=200, verbose_name='Особенности ухода'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='peresadka',
            field=models.CharField(blank=True, max_length=200, verbose_name='Пересадка'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='photo',
            field=models.ImageField(blank=True, upload_to='preview/cveti'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='pochva',
            field=models.CharField(blank=True, max_length=200, verbose_name='Почва'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='poliv',
            field=models.CharField(blank=True, max_length=200, verbose_name='Полив'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='polza',
            field=models.CharField(blank=True, max_length=400, verbose_name='Польза ростения'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 10, 18, 33, 10, 414384), blank=True, verbose_name='Дата публикации'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='sposob_razmnogeniya',
            field=models.CharField(blank=True, max_length=200, verbose_name='Способ размножения'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='svet',
            field=models.CharField(blank=True, max_length=200, verbose_name='Свет'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='temperatera',
            field=models.CharField(blank=True, max_length=200, verbose_name='Температура'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='vlajnost_vozduha',
            field=models.CharField(blank=True, max_length=200, verbose_name='Влажность воздуха'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='kommentariycvetka',
            name='CvetiKatalog',
            field=models.ForeignKey(verbose_name='Каталог цветов', to='KatalogCvetov.CvetiKatalog'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='kommentariycvetka',
            name='kommentariy',
            field=models.CharField(max_length=200, verbose_name='Комментарий ростения'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reytingcvetka',
            name='cveti_katalog',
            field=models.ForeignKey(verbose_name='Каталог цветов', to='KatalogCvetov.CvetiKatalog'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reytingcvetka',
            name='reyting',
            field=models.IntegerField(default=0, verbose_name='Рейтинг'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vidirasteniy',
            name='name_vida',
            field=models.CharField(max_length=200, verbose_name='Вид растения'),
            preserve_default=True,
        ),
    ]
