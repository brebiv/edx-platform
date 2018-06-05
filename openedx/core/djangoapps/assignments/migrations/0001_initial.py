# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-05 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseRunAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_run_id', models.CharField(max_length=100)),
                ('block_id', models.CharField(max_length=100)),
                ('display_name', models.CharField(max_length=255)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='courserunassignment',
            unique_together=set([('course_run_id', 'block_id')]),
        ),
    ]
