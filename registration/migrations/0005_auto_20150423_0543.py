# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20150423_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='program',
            field=models.ManyToManyField(to='registration.Program', blank=True),
        ),
    ]
