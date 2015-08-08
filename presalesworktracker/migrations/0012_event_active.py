# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presalesworktracker', '0011_auto_20150710_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
