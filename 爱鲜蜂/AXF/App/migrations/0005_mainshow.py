# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-02 03:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20180601_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=30)),
                ('trackid', models.CharField(max_length=20)),
                ('categoryid', models.CharField(max_length=20)),
                ('brandname', models.CharField(max_length=20)),
                ('img1', models.CharField(max_length=200)),
                ('childcid1', models.CharField(max_length=20)),
                ('productid1', models.CharField(max_length=20)),
                ('longname1', models.CharField(max_length=50)),
                ('price1', models.CharField(max_length=20)),
                ('marketprice1', models.CharField(max_length=20)),
                ('img2', models.CharField(max_length=200)),
                ('childcid2', models.CharField(max_length=20)),
                ('productid2', models.CharField(max_length=20)),
                ('longname2', models.CharField(max_length=50)),
                ('price2', models.CharField(max_length=20)),
                ('marketprice2', models.CharField(max_length=20)),
                ('img3', models.CharField(max_length=200)),
                ('childcid3', models.CharField(max_length=20)),
                ('productid3', models.CharField(max_length=20)),
                ('longname3', models.CharField(max_length=50)),
                ('price3', models.CharField(max_length=20)),
                ('marketprice3', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'axf_mainshow',
            },
        ),
    ]
