# Generated by Django 2.0.4 on 2018-04-20 23:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cuerpo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fechaCreacion',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 20, 23, 22, 32, 679415, tzinfo=utc)),
        ),
    ]