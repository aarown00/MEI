# Generated by Django 5.0.6 on 2024-06-08 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_it_request_screenshot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='it_request',
            name='screenshot',
        ),
        migrations.AlterField(
            model_name='it_request',
            name='eq_type',
            field=models.CharField(choices=[('Desktop', 'Desktop'), ('Laptop', 'Laptop'), ('Printer', 'Printer'), ('Network Devices', 'Network devices'), ('Peripherals', 'Peripherals')], default='Desktop', max_length=100),
        ),
        migrations.AlterField(
            model_name='it_request',
            name='status',
            field=models.CharField(choices=[('Requested', 'Requested'), ('Ongoing', 'Ongoing'), ('Completed', 'Completed')], default='Requested', max_length=100),
        ),
    ]
