# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-23 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bigaim',
            name='description',
        ),
        migrations.RemoveField(
            model_name='clinicaldepartment',
            name='description',
        ),
        migrations.RemoveField(
            model_name='focusarea',
            name='description',
        ),
        migrations.AlterField(
            model_name='bigaim',
            name='sort_order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='clinicalarea',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='clinicaldepartment',
            name='sort_order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='clinicalsetting',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='expertise',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='focusarea',
            name='sort_order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='position',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='qi_interest',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='safetytarget',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='suffix',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
