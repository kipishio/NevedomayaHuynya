# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KatalogCvetov', '0008_auto_20150707_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='VidiRosteniy',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name_vida', models.CharField(verbose_name='Вид растения', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cvetikatalog',
            name='VidiRosteniy',
            field=models.ForeignKey(default=1, to='KatalogCvetov.VidiRosteniy'),
            preserve_default=False,
        ),
    ]
