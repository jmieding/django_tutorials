# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20151213_0342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=400)),
                ('author', models.CharField(max_length=40)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(to='articles.Post')),
            ],
        ),
    ]
