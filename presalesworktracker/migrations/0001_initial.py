# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Year', models.CharField(max_length=4)),
                ('Quarter', models.CharField(max_length=1)),
                ('Date', models.DateTimeField(verbose_name=b'Date')),
                ('Type', models.CharField(max_length=100)),
                ('RSMOverlayLocal', models.CharField(max_length=50)),
                ('Region', models.CharField(max_length=20)),
                ('LocalPreSalesinvolved', models.NullBooleanField()),
                ('LocalPreSalesInvolve', models.BooleanField()),
                ('NameofSE', models.CharField(max_length=50)),
                ('IfnoSEwhynot', models.CharField(max_length=50)),
                ('ActiveRoleWhatKind', models.CharField(max_length=50)),
                ('GovSolutions', models.BooleanField()),
                ('EffortInclPrep', models.CharField(max_length=12)),
                ('Whatwasgoodwhatbad', models.TextField()),
            ],
        ),
    ]
