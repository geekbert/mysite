# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presalesworktracker', '0003_auto_20150710_2011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='LocalPreSalesinvolved',
            new_name='LocalPreSalesInvolved',
        ),
        migrations.RemoveField(
            model_name='work',
            name='LocalPreSalesInvolve',
        ),
        migrations.RemoveField(
            model_name='work',
            name='Whatwasgoodwhatbad',
        ),
        migrations.AddField(
            model_name='work',
            name='WhatWasGoodWhatBad',
            field=models.CharField(default='unknown', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='work',
            name='ActiveRoleWhatKind',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='work',
            name='Date',
            field=models.DateField(verbose_name=b'Date'),
        ),
    ]
