# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presalesworktracker', '0004_auto_20150710_2029'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='work',
            new_name='Events',
        ),
    ]
