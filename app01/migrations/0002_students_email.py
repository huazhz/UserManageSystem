# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 04:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='email',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
