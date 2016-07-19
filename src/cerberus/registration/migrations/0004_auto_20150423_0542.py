# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20150423_0050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='program',
        ),
        migrations.AddField(
            model_name='student',
            name='program',
            field=models.ManyToManyField(to='registration.Program', null=True, blank=True),
        ),
    ]
