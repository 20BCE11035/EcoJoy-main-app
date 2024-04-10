# Generated by Django 3.2.14 on 2022-07-20 19:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_blogs_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogs",
            name="time",
        ),
        migrations.AddField(
            model_name="blogs",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(2022, 7, 20, 19, 51, 58, 941794, tzinfo=utc),
            ),
            preserve_default=False,
        ),
    ]