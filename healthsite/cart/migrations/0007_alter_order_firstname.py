# Generated by Django 4.0.1 on 2022-04-26 00:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_remove_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='firstname',
            field=models.CharField(max_length=45, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]
