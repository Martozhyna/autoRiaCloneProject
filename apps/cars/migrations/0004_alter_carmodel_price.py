# Generated by Django 4.2.1 on 2023-05-21 02:08

from django.db import migrations

import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_carmodel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='price',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='USD', max_digits=14),
        ),
    ]
