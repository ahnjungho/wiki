# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150629_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='category',
            field=models.ForeignKey(to='pages.Category', default=None, null=True),
        ),
    ]
