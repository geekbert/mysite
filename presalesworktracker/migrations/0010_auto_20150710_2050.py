# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presalesworktracker', '0009_auto_20150710_2045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='What_was_Good',
            new_name='Comment',
        ),
        migrations.AlterField(
            model_name='event',
            name='Effort_Incl_Prep',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='If_no_SE_why_not',
            field=models.CharField(max_length=100),
        ),
    ]
