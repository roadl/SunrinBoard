# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=1, default='FR', choices=[('QU', 'Question'), ('FR', 'Free'), ('TI', 'Tip')]),
        ),
    ]
