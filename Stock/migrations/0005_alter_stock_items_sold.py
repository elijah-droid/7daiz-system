# Generated by Django 3.2 on 2023-07-08 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0004_stock_alert_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='Items_Sold',
            field=models.PositiveIntegerField(default=0),
        ),
    ]