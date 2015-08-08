# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Joke',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('situation', models.CharField(max_length=150)),
                ('joke', models.CharField(max_length=900)),
                ('pub_date', models.DateField(default=datetime.date.today, blank=True)),
                ('tag', models.CharField(max_length=4)),
                ('rank', models.CharField(max_length=4, null=True, blank=True)),
            ],
        ),
    ]
