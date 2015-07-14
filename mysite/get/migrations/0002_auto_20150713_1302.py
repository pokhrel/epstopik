# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('choice', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('question', models.CharField(max_length=50)),
                ('answer', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='exercisechoice',
            name='question',
            field=models.ForeignKey(to='get.ExerciseQuestion'),
        ),
    ]
