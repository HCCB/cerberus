# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#  from django.db import models
from django.db import migrations


def forwards(apps, schema_editor):
    print "adding initial data"


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards),
    ]
