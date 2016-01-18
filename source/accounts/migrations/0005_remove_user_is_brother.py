# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_is_brother'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_brother',
        ),
    ]
