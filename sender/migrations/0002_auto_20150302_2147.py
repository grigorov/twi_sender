# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sender', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitteraccount',
            name='name',
            field=models.CharField(verbose_name='Twitter Name/Nick', help_text='Твиттер имя', max_length=250, editable=False),
            preserve_default=True,
        ),
    ]
