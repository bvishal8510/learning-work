# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-03 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_auto_20180203_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.ImageField(upload_to=''),
        ),
    ]
