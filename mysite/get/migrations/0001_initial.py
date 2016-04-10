# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name_en', models.CharField(max_length=50)),
                ('name_ne', models.CharField(max_length=50)),
                ('questions', models.IntegerField()),
                ('filename', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='NewsEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title_en', models.CharField(max_length=100)),
                ('title_ne', models.CharField(max_length=100)),
                ('content_en', models.CharField(max_length=500)),
                ('content_ne', models.CharField(max_length=500)),
                ('date', models.DateField(verbose_name='pub_date')),
            ],
        ),
    ]
