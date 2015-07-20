# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KatalogCvetov', '0011_auto_20150710_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvetikatalog',
            name='VidiRasteniy',
            field=models.ForeignKey(verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4\xd1\x8b \xd1\x80\xd0\xb0\xd1\x81\xd1\x82\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb9', to='KatalogCvetov.VidiRasteniy'),
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='cena',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='coderjat',
            field=models.TextField(verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb6\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x80\xd0\xbe\xd1\x81\xd1\x82\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='name_rosteniya',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x86\xd0\xb2\xd0\xb5\xd1\x82\xd0\xba\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='opisanie',
            field=models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='osobennosty_uhod',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9e\xd1\x81\xd0\xbe\xd0\xb1\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8 \xd1\x83\xd1\x85\xd0\xbe\xd0\xb4\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='peresadka',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9f\xd0\xb5\xd1\x80\xd0\xb5\xd1\x81\xd0\xb0\xd0\xb4\xd0\xba\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='photo',
            field=models.ImageField(upload_to=b'preview/cveti'),
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='pochva',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x87\xd0\xb2\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='poliv',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd0\xb8\xd0\xb2'),
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='polza',
            field=models.CharField(max_length=400, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xb0 \xd1\x80\xd0\xbe\xd1\x81\xd1\x82\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='sposob_razmnogeniya',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\xa1\xd0\xbf\xd0\xbe\xd1\x81\xd0\xbe\xd0\xb1 \xd1\x80\xd0\xb0\xd0\xb7\xd0\xbc\xd0\xbd\xd0\xbe\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='svet',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\xa1\xd0\xb2\xd0\xb5\xd1\x82'),
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='temperatera',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbc\xd0\xbf\xd0\xb5\xd1\x80\xd0\xb0\xd1\x82\xd1\x83\xd1\x80\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='vlajnost_vozduha',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xbb\xd0\xb0\xd0\xb6\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c \xd0\xb2\xd0\xbe\xd0\xb7\xd0\xb4\xd1\x83\xd1\x85\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='kommentariycvetka',
            name='CvetiKatalog',
            field=models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb0\xd0\xbb\xd0\xbe\xd0\xb3 \xd1\x86\xd0\xb2\xd0\xb5\xd1\x82\xd0\xbe\xd0\xb2', to='KatalogCvetov.CvetiKatalog'),
        ),
        migrations.AlterField(
            model_name='kommentariycvetka',
            name='kommentariy',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb9 \xd1\x80\xd0\xbe\xd1\x81\xd1\x82\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='reytingcvetka',
            name='cveti_katalog',
            field=models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb0\xd0\xbb\xd0\xbe\xd0\xb3 \xd1\x86\xd0\xb2\xd0\xb5\xd1\x82\xd0\xbe\xd0\xb2', to='KatalogCvetov.CvetiKatalog'),
        ),
        migrations.AlterField(
            model_name='reytingcvetka',
            name='reyting',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb9\xd1\x82\xd0\xb8\xd0\xbd\xd0\xb3'),
        ),
        migrations.AlterField(
            model_name='vidirasteniy',
            name='name_vida',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x80\xd0\xb0\xd1\x81\xd1\x82\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
    ]
