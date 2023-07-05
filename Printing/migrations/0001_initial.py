# Generated by Django 3.2 on 2023-07-04 08:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Branches', '0002_initial'),
        ('Papers', '0001_initial'),
        ('Employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Printing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('No_of_Papers', models.PositiveIntegerField()),
                ('Amount_Paid', models.PositiveIntegerField()),
                ('Branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Branches.branch')),
                ('Paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Papers.paper')),
                ('Printed_By', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employees.employee')),
            ],
        ),
    ]