# Generated by Django 3.2.5 on 2021-08-23 13:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20210823_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 25, 13, 48, 8, 608873, tzinfo=utc)),
        ),
    ]
