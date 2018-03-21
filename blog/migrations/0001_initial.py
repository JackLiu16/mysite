# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', ckeditor.fields.RichTextField(verbose_name=b'\xe6\xad\xa3\xe6\x96\x87')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe4\xbf\x9d\xe5\xad\x98\xe6\x97\xa5\xe6\x9c\x9f')),
            ],
        ),
    ]
