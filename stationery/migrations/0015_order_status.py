# Generated by Django 3.1.4 on 2021-07-27 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationery', '0014_order_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('order pending', 'order pending'), ('order received', 'order received'), ('order processing', 'order processing'), ('order completed', 'order completed'), ('order cancelled', 'order cancelled')], default='order received', max_length=255),
        ),
    ]