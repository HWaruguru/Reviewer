# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-10-26 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0003_auto_20211026_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
