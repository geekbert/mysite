# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presalesworktracker', '0012_event_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='If_no_SE_why_not',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
