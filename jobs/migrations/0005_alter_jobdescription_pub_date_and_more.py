# Generated by Django 4.1.5 on 2023-01-20 05:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_rename_discription_portal_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdescription',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 5, 10, 51, 918849, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='title',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 5, 10, 51, 918849, tzinfo=datetime.timezone.utc)),
        ),
    ]
