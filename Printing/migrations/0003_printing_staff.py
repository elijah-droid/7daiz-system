# Generated by Django 4.2.7 on 2023-12-23 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0003_employee_large_format_attribute_employee_printing_and_more'),
        ('Printing', '0002_remove_printing_printed_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='printing',
            name='Staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_print', to='Employees.employee'),
        ),
    ]