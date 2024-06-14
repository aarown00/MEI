# Generated by Django 5.0.6 on 2024-06-14 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0023_alter_it_request_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='it_request',
            name='department',
            field=models.CharField(choices=[('Human Resources (HR)', 'Human resources (hr)'), ('Finance/Accounting', 'Finance/accounting'), ('Information Technology (IT)', 'Information technology (it)'), ('Marketing/Sales', 'Marketing/sales'), ('Operations', 'Operations'), ('Engineering', 'Engineering')], max_length=100),
        ),
        migrations.AlterField(
            model_name='it_request',
            name='status',
            field=models.CharField(choices=[('Waiting', 'Waiting'), ('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Waiting', max_length=100),
        ),
    ]
