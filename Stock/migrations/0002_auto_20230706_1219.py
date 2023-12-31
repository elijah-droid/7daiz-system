# Generated by Django 3.2 on 2023-07-06 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Branches', '0008_branch_name'),
        ('Stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='Branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Branches.branch'),
        ),
        migrations.AddField(
            model_name='stock',
            name='Price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
