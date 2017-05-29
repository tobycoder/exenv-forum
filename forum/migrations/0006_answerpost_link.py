# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 20:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20170529_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerpost',
            name='link',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='forum.QuestionPost'),
            preserve_default=False,
        ),
    ]
