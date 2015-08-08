# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presalesworktracker', '0006_auto_20150710_2035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='NameofSE',
            new_name='Name_of_SE',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='WhatWasGoodWhatBad',
            new_name='What_was_Good',
        ),
    ]
