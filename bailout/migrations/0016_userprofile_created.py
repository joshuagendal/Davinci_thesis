# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bailout', '0015_rating_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
