# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='studentID',
            field=models.CharField(default='no ID', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='studentName',
            field=models.CharField(default='no name', max_length=50),
            preserve_default=False,
        ),
    ]
