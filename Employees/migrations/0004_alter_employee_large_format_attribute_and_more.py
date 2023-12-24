# Generated by Django 4.2.7 on 2023-12-23 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Largeformat', '0003_remove_largeformatprinting_amountpaid_and_more'),
        ('Printing', '0003_printing_staff'),
        ('Sales', '0003_sale_staff'),
        ('Employees', '0003_employee_large_format_attribute_employee_printing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='large_format_attribute',
            field=models.ManyToManyField(blank=True, related_name='employee_largeprints', to='Largeformat.largeformatprinting'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='printing',
            field=models.ManyToManyField(blank=True, to='Printing.printing'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='printing_attribute',
            field=models.ManyToManyField(blank=True, related_name='employee_prints', to='Printing.printing'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='sales_attribute',
            field=models.ManyToManyField(blank=True, to='Sales.sale'),
        ),
    ]
