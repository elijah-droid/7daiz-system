# Generated by Django 4.2.7 on 2023-12-15 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
