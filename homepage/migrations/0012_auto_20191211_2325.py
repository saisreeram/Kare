# Generated by Django 2.2.5 on 2019-12-11 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_auto_20191211_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='donatemoney',
            name='paypal_transaction',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='verification',
            name='hit',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 11, 23, 25, 56, 3428)),
        ),
    ]
