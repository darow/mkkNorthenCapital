# Generated by Django 2.2.3 on 2019-09-25 19:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('site_pages', '0002_customer_request_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_request',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 25, 19, 13, 12, 624473, tzinfo=utc), verbose_name='Время создания'),
        ),
    ]