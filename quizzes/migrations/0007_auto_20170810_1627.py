# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-10 20:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0006_studentquizresult__q_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermembership',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to=settings.AUTH_USER_MODEL),
        ),
    ]
