# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-10 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0004_auto_20170810_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='out_of',
        ),
        migrations.AddField(
            model_name='quiz',
            name='_cat_list',
            field=models.TextField(null=True),
        ),
    ]
