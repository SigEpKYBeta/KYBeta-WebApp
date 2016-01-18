# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('school_classification', models.CharField(max_length=10, choices=[('FRESHMAN', 'Freshman'), ('SOPHOMORE', 'Sophomore'), ('JUNIOR', 'Junior'), ('SENIOR', 'Senior')])),
                ('challenge_classification', models.CharField(max_length=20, choices=[('SIGMA', 'Sigma'), ('PHI', 'Phi'), ('Epsilon', 'Epsilon'), ('BROTHER_MENTOR', 'Brother Mentor')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
