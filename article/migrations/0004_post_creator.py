# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0003_auto_20151023_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='creator',
            field=models.ForeignKey(related_name='user_post', default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
