# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get', '0002_auto_20150713_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercisechoice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='exercisequestion',
            name='answer',
        ),
        migrations.AddField(
            model_name='exercisequestion',
            name='answer',
            field=models.ManyToManyField(to='get.ExerciseChoice'),
        ),
    ]
