# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 21:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textifai', '0002_text_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='text',
            options={'ordering': ['time_created']},
        ),
    ]
