# Generated by Django 3.0.3 on 2020-03-14 20:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('twts', '0005_auto_20200314_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 14, 20, 25, 23, 427104, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='twt',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 14, 20, 25, 23, 427104, tzinfo=utc), verbose_name='date published'),
        ),
    ]
