# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20150422_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='program',
            field=models.ForeignKey(blank=True, to='registration.Program', null=True),
        ),
    ]
