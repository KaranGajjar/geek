# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-17 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geek_bp_xprofile_fields',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]
