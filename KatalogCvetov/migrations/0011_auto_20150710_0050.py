# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KatalogCvetov', '0010_auto_20150708_1436'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cvetikatalog',
            options={'verbose_name_plural': 'Каталог цветов', 'verbose_name': 'Каталог цветов'},
        ),
        migrations.AlterModelOptions(
            name='kommentariycvetka',
            options={'verbose_name_plural': 'Комметарии', 'verbose_name': 'Комметарий'},
        ),
        migrations.AlterModelOptions(
            name='reytingcvetka',
            options={'verbose_name_plural': 'Рейтинги растиний', 'verbose_name': 'Рейтинг растения'},
        ),
        migrations.AlterModelOptions(
            name='vidirasteniy',
            options={'verbose_name_plural': 'Вид растения', 'verbose_name': 'Вид растения'},
        ),
        migrations.AddField(
            model_name='cvetikatalog',
            name='photo',
            field=models.ImageField(default=1, upload_to='cveti'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cvetikatalog',
            name='VidiRasteniy',
            field=models.ForeignKey(to='KatalogCvetov.VidiRasteniy', verbose_name='Виды растений'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='kommentariycvetka',
            name='CvetiKatalog',
            field=models.ForeignKey(to='KatalogCvetov.CvetiKatalog', verbose_name='Каталог цветов'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reytingcvetka',
            name='cveti_katalog',
            field=models.ForeignKey(to='KatalogCvetov.CvetiKatalog', verbose_name='Каталог цветов'),
            preserve_default=True,
        ),
    ]
