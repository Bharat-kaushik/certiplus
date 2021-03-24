# Generated by Django 3.1.7 on 2021-03-23 15:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userPlus', '0008_auto_20210323_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='key',
            field=models.CharField(default='8d6e0852-6', editable=False, max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='key',
            field=models.CharField(default='43c5db8f-8', editable=False, max_length=10, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]