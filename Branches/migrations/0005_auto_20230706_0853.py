# Generated by Django 3.2 on 2023-07-06 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Printing', '0001_initial'),
        ('Reports', '0003_auto_20230704_1724'),
        ('Employees', '0001_initial'),
        ('Sales', '0001_initial'),
        ('Stock', '0001_initial'),
        ('Branches', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='Cashier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='branch_cashier', to='Employees.employee'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='Printing',
            field=models.ManyToManyField(blank=True, to='Printing.Printing'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='Reports',
            field=models.ManyToManyField(blank=True, to='Reports.Report'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='Sales',
            field=models.ManyToManyField(blank=True, to='Sales.Sale'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='Stock',
            field=models.ManyToManyField(blank=True, to='Stock.Stock'),
        ),
    ]