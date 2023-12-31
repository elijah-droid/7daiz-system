# Generated by Django 4.2.7 on 2023-12-23 09:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0003_employee_large_format_attribute_employee_printing_and_more'),
        ('Largeformat', '0002_alter_roll_buying_price_alter_roll_meters_left_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='largeformatprinting',
            name='AmountPaid',
        ),
        migrations.RemoveField(
            model_name='largeformatprinting',
            name='Meters_Printed',
        ),
        migrations.RemoveField(
            model_name='roll',
            name='Buying_Price',
        ),
        migrations.AddField(
            model_name='largeformatprinting',
            name='Amount_Paid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='largeformatprinting',
            name='Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='largeformatprinting',
            name='Height_Printed',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='largeformatprinting',
            name='Staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_largeprint', to='Employees.employee'),
        ),
        migrations.AddField(
            model_name='largeformatprinting',
            name='Total_Meters_Printed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='largeformatprinting',
            name='Width_Printed',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
