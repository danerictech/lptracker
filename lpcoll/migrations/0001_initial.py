# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license_plate', models.CharField(max_length=20)),
                ('car_brand', models.CharField(max_length=100)),
                ('car_model', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('transit_date', models.DateTimeField()),
            ],
        ),
    ]
