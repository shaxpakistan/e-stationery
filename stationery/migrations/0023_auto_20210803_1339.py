# Generated by Django 3.1.4 on 2021-08-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationery', '0022_auto_20210803_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationery',
            name='approve_ID',
            field=models.BooleanField(),
        ),
    ]