# Generated by Django 3.1.7 on 2021-03-24 15:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userPlus', '0014_auto_20210324_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='key',
            field=models.CharField(default='3ba38ba0-3', editable=False, max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='key',
            field=models.CharField(default='f6638d4c-d', editable=False, max_length=10, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]