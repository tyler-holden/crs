# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-11 19:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0009_evaluation_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='status',
        ),
    ]
