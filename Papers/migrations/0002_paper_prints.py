# Generated by Django 3.2 on 2023-07-04 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Printing', '0001_initial'),
        ('Papers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='Prints',
            field=models.ManyToManyField(to='Printing.Printing'),
        ),
    ]
