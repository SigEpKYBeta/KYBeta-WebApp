# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fines', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fine',
            name='status',
            field=models.CharField(choices=[('UNPAID', 'Unpaid'), ('PAID', 'Paid'), ('WAIVED', 'Waived')], max_length=10, default='UNPAID'),
            preserve_default=False,
        ),
    ]
