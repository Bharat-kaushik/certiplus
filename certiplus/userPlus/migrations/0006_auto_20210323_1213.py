# Generated by Django 3.1.7 on 2021-03-23 06:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userPlus', '0005_auto_20210322_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logo',
            name='logo',
        ),
        migrations.AlterField(
            model_name='company',
            name='key',
            field=models.CharField(default='12746d4e-2', editable=False, max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='key',
            field=models.CharField(default='5c153c08-9', editable=False, max_length=10, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]
