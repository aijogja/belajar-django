# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20151030_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(default=b'p', max_length=1, choices=[(b'd', b'Draft'), (b'p', b'Published'), (b'w', b'Withdrawn')]),
        ),
    ]
