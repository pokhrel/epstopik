# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get', '0003_auto_20150713_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercisequestion',
            old_name='answer',
            new_name='answers',
        ),
    ]
