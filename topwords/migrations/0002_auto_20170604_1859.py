# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-04 10:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topwords', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotpoint',
            name='sn',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 4, 18, 59, 40, 348969)),
        ),
    ]
