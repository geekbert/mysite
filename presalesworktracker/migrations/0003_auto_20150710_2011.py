# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presalesworktracker', '0002_auto_20150710_2007'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='presalesworktracker',
            new_name='work',
        ),
    ]
