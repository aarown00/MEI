# Generated by Django 5.0.6 on 2024-06-08 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0021_alter_it_request_screenshot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='it_request',
            name='screenshot',
        ),
        migrations.AddField(
            model_name='it_request',
            name='upload',
            field=models.ImageField(blank=True, null=True, upload_to='user_uploads/'),
        ),
    ]