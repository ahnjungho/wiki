# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20150710_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='category',
            field=models.ForeignKey(default=None, to='pages.Category', blank=True, null=True),
        ),
    ]
