# Generated by Django 4.2.1 on 2023-05-12 22:21

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)])),
                ('model', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)])),
                ('city_of_sale', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)])),
                ('year', models.IntegerField()),
                ('price', models.IntegerField()),
                ('created_add', models.DateTimeField(auto_now_add=True)),
                ('updated_add', models.DateTimeField(auto_now=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]
