# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presalesworktracker', '0013_auto_20150712_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Customer',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='Active_Role_What_Kind',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='Effort_Incl_Prep',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='Region',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
