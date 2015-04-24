# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street1', models.CharField(default=b'', max_length=60)),
                ('street2', models.CharField(default=b'', max_length=60)),
                ('city', models.CharField(default=b'Butuan City', max_length=60)),
                ('province', models.CharField(default=b'Agusan del Norte', max_length=60)),
                ('zip', models.CharField(default=b'8600', max_length=10)),
                ('kind', models.IntegerField(default=1, choices=[(1, b'Home'), (2, b'Work'), (3, b'Permanent')])),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=60)),
                ('short_name', models.CharField(default=b'', max_length=30)),
                ('head_title', models.CharField(default=b'Dean', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30, null=True, blank=True)),
                ('name_suffix', models.CharField(max_length=10, null=True, blank=True)),
                ('gender', models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
            ],
            options={
                'ordering': ['last_name', 'first_name', 'middle_name'],
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=20)),
                ('kind', models.IntegerField(default=1, verbose_name=b'Type', choices=[(1, b'Home'), (2, b'Work'), (3, b'Mobile'), (4, b'Fax'), (5, b'Other')])),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('major', models.CharField(max_length=60, null=True, blank=True)),
                ('description', models.CharField(max_length=200, null=True, blank=True)),
                ('short_name', models.CharField(max_length=30)),
                ('department', models.ForeignKey(to='registration.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=30)),
                ('series', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['series', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_name', models.CharField(default=b'', max_length=20)),
                ('description', models.CharField(default=b'', max_length=60)),
                ('units', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='registration.Person')),
                ('occupation', models.CharField(default=b'', max_length=30)),
                ('relationship', models.CharField(default=b'Father', max_length=30)),
                ('emergency_contact', models.CharField(max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')])),
            ],
            bases=('registration.person',),
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='registration.Person')),
                ('kind', models.IntegerField(verbose_name=b'Type', choices=[(1, b'Full-time'), (2, b'Part-time')])),
                ('department', models.ForeignKey(related_name='department', to='registration.Department')),
            ],
            bases=('registration.person',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='registration.Person')),
                ('civil_status', models.CharField(default=b'Single', max_length=20)),
                ('citizenship', models.CharField(default=b'Filipino', max_length=30)),
                ('religion', models.CharField(default=b'Roman Catholic', max_length=30)),
                ('birthdate', models.DateField(default=datetime.date.today)),
                ('birthplace', models.CharField(default=b'', max_length=100)),
                ('enrollment_type', models.IntegerField(default=1, choices=[(1, b'New'), (2, b'Old'), (3, b'Returnee'), (4, b'Cross-Enrollee')])),
                ('school_level', models.IntegerField(default=2, choices=[(1, b'Grade School'), (2, b'High School'), (3, b'College'), (4, b'Graduate'), (5, b'Doctorate')])),
                ('year_level', models.IntegerField(default=1)),
                ('id_number', models.CharField(default=b'', max_length=20, blank=True)),
                ('department', models.ForeignKey(to='registration.Department', null=True)),
                ('program', models.ForeignKey(to='registration.Program', null=True)),
            ],
            bases=('registration.person',),
        ),
        migrations.AddField(
            model_name='phone',
            name='owner',
            field=models.ForeignKey(to='registration.Person'),
        ),
        migrations.AddField(
            model_name='address',
            name='owner',
            field=models.ForeignKey(to='registration.Person'),
        ),
        migrations.AddField(
            model_name='guardian',
            name='ward',
            field=models.ForeignKey(to='registration.Student', null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='head',
            field=models.OneToOneField(related_name='dean_or_principal', null=True, blank=True, to='registration.Instructor'),
        ),
    ]
