# Generated by Django 3.2 on 2023-07-06 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0003_stock_items_sold'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='Alert_Level',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
