# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 08:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_plan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='travel',
            name='user_id_join',
        ),
        migrations.AddField(
            model_name='join',
            name='travel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='join_travel', to='travel_plan.Travel'),
        ),
        migrations.AddField(
            model_name='join',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='join_user', to='travel_plan.User'),
        ),
    ]