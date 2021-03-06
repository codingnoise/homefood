# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-08-05 16:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('interview_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('interview_date', models.CharField(default='', max_length=30)),
                ('interview_time', models.CharField(default='', max_length=30)),
                ('interview_topic', models.CharField(default=b'general_interview', max_length=50)),
                ('interview_duration', models.CharField(default=b'30', max_length=30)),
                ('interviewer_email', models.EmailField(max_length=254)),
                ('interview_status', models.CharField(default=b'scheduled', max_length=30)),
                ('interview_metadata', models.CharField(default='', max_length=30000)),
                ('interviewee_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
