# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-25 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fast_excute', '0003_fastexcude_bar_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fastexcude',
            name='shell',
            field=models.CharField(max_length=255, verbose_name='命令（如有多个命令，一行写一个命令，按序执行）'),
        ),
    ]