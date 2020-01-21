# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-26 23:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='Updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]