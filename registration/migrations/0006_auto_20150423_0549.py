# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20150423_0543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='program',
        ),
        migrations.AddField(
            model_name='student',
            name='program',
            field=models.ForeignKey(blank=True, to='registration.Program', null=True),
        ),
    ]
