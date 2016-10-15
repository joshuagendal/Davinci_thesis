# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-15 18:31
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('bailout', '0019_auto_20161015_0349'),
    ]

    operations = [
        migrations.AddField(
            model_name='bailout',
            name='state_ab',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='state',
            field=localflavor.us.models.USStateField(default=1),
            preserve_default=False,
        ),
    ]
