# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presalesworktracker', '0010_auto_20150710_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Comment',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
