# Generated by Django 4.2.7 on 2023-12-23 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Largeformat', '0004_roll_width'),
    ]

    operations = [
        migrations.AlterField(
            model_name='largeformatprinting',
            name='Total_Meters_Printed',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
