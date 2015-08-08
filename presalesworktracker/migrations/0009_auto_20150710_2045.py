# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presalesworktracker', '0008_auto_20150710_2042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='Type',
            new_name='Event_Type',
        ),
    ]
