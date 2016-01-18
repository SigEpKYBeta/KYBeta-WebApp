# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fines', '0002_fine_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='fine',
            name='created',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2016, 1, 18, 17, 22, 17, 257726, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
