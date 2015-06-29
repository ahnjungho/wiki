# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20150629_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='slug',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
