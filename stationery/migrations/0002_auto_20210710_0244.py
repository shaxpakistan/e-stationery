# Generated by Django 3.1.4 on 2021-07-09 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stationery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stationery',
            options={'verbose_name_plural': 'Stationeries'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='subtotal',
        ),
    ]
