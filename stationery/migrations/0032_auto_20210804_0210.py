# Generated by Django 3.1.4 on 2021-08-03 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationery', '0031_auto_20210804_0206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stationery',
            name='approval01',
        ),
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='stationery',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
