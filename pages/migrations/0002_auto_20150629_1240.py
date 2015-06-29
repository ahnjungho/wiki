# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 29, 12, 40, 18, 993375, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 29, 12, 40, 25, 569420, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
