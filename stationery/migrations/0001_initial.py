# Generated by Django 3.1.4 on 2021-07-09 23:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Approve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.PositiveIntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_name', models.CharField(choices=[('Office-Supply', 'Office-Supply'), ('Folders', 'Folders'), ('Tapes', 'Tapes'), ('Ink', 'Ink'), ('Craft', 'Craft'), ('Market', 'Market'), ('Clips', 'Clips'), ('Artist-Corner', 'Artist-Corner'), ('Paper', 'Paper'), ('Pencils', 'Pencils'), ('Colours', 'Colours'), ('Pens', 'Pens'), ('Books', 'Books'), ('Acts', 'Acts'), ('Refills', 'Refills'), ('Cases', 'Cases'), ('ID`s', 'ID`s')], max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_type', models.CharField(max_length=255)),
                ('doc_cost', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locatio_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Stationery',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('profile', models.ImageField(upload_to='stationery/')),
                ('location', models.CharField(max_length=100)),
                ('motto', models.TextField(default='Welcome to our worth stationery ever, get service on time. Here we value your choice')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Stationaries',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=255)),
                ('stock_type', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('stationery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stationery.stationery')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(blank=True, choices=[('printing', 'printing'), ('scanning', 'scanning'), ('emailing', 'emailing')], max_length=100, null=None)),
                ('task_type', models.CharField(blank=True, choices=[('individual', 'individual'), ('group', 'group'), ('report', 'report'), ('research', 'research'), ('paper', 'paper')], max_length=150, null=None)),
                ('stationery', models.ForeignKey(blank=True, null=None, on_delete=django.db.models.deletion.CASCADE, to='stationery.stationery')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.CharField(max_length=255)),
                ('stationery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stationery.stationery')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_desc', models.TextField()),
                ('item_img', models.ImageField(upload_to='products/')),
                ('item_available', models.PositiveIntegerField(default=0)),
                ('item_price', models.PositiveIntegerField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('item_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stationery.category')),
                ('stat_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_posted', to='stationery.stationery')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveIntegerField(null=True)),
                ('destination', models.CharField(blank=True, max_length=100, null=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('subtotal', models.PositiveIntegerField()),
                ('totalpay', models.PositiveIntegerField()),
                ('cart', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stationery.cart')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('stationery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stationery.stationery')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('rate', models.PositiveIntegerField()),
                ('subtotal', models.PositiveBigIntegerField(blank=True, null=True)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stationery.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stationery.product')),
            ],
        ),
    ]
