# Generated by Django 3.1.4 on 2021-08-03 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationery', '0023_auto_20210803_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationery',
            name='approve_ID',
            field=models.BooleanField(default=False),
        ),
    ]
