# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presalesworktracker', '0014_auto_20150712_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='POC',
            field=models.BooleanField(default='FALSE'),
            preserve_default=False,
        ),
    ]
