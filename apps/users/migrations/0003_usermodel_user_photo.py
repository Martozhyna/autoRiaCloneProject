# Generated by Django 4.2.1 on 2023-05-15 20:33

from django.db import migrations, models

import core.services.uppload_user_photo_service


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profilemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='user_photo',
            field=models.ImageField(blank=True, upload_to=core.services.uppload_user_photo_service.upload_to),
        ),
    ]
