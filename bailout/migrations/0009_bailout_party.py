# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bailout', '0008_auto_20160927_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='bailout',
            name='party',
            field=models.FloatField(blank=True, max_length=25, null=True),
        ),
    ]
