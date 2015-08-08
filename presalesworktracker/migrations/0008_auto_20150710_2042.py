# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presalesworktracker', '0007_auto_20150710_2039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='ActiveRoleWhatKind',
            new_name='Active_Role_What_Kind',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='EffortInclPrep',
            new_name='Effort_Incl_Prep',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='IfnoSEwhynot',
            new_name='If_no_SE_why_not',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='LocalPreSalesInvolved',
            new_name='Local_PreSales_Involved',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='RSMOverlayLocal',
            new_name='RSM_Overlay_Local',
        ),
    ]
