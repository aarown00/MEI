# Generated by Django 5.0.6 on 2024-06-08 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0019_alter_it_request_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='it_request',
            name='screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='user_screenshots/'),
        ),
    ]