# Generated by Django 3.1.4 on 2021-08-03 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationery', '0028_auto_20210804_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationery',
            name='status',
            field=models.BooleanField(),
        ),
    ]