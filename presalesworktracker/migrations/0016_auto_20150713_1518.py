# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presalesworktracker', '0015_event_poc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='POC',
            field=models.BooleanField(default=None),
        ),
    ]
