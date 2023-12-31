# Generated by Django 3.2 on 2023-07-04 08:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Printing', '0001_initial'),
        ('Branches', '0003_branch_printing'),
        ('Sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Grand_Total', models.PositiveIntegerField()),
                ('Cash', models.PositiveIntegerField()),
                ('Branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Branches.branch')),
                ('Printing', models.ManyToManyField(to='Printing.Printing')),
                ('Sales', models.ManyToManyField(to='Sales.Sale')),
            ],
        ),
    ]
