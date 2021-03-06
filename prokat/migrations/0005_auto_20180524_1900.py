# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-24 16:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prokat', '0004_auto_20180521_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ваше имя')),
                ('phone', models.IntegerField(verbose_name='Телефон')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prokat.Product', verbose_name='Название снаряжения')),
            ],
        ),
        migrations.DeleteModel(
            name='ProductManager',
        ),
    ]
