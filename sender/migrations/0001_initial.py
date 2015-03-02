# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterAccount',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Twitter Name/Nick', max_length=250, help_text='Твиттер имя')),
                ('id_twitter', models.IntegerField(editable=False, unique=True)),
                ('consumer_key', models.CharField(verbose_name='Consumer key', max_length=250, help_text='dev.twitter.com/app необходимо получить ключи')),
                ('consumer_secret', models.CharField(verbose_name='Consumer secret', max_length=250)),
                ('access_token', models.CharField(verbose_name='Access token', max_length=250)),
                ('access_token_secret', models.CharField(verbose_name='Access token Secret', max_length=250)),
                ('active', models.BooleanField(default=False, editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
