# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-11 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_level',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
