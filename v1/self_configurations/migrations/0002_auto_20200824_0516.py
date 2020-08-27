# Generated by Django 3.1 on 2020-08-24 02:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('self_configurations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selfconfiguration',
            name='daily_confirmation_rate',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='selfconfiguration',
            name='default_transaction_fee',
            field=models.PositiveBigIntegerField(validators=[django.core.validators.MaxValueValidator(281474976710656), django.core.validators.MinValueValidator(1)]),
        ),
    ]