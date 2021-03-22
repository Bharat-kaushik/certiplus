# Generated by Django 3.1.7 on 2021-03-22 09:24

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userPlus', '0004_auto_20210322_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='key',
            field=models.CharField(default='fcf1d72f-2', editable=False, max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='key',
            field=models.CharField(default='378697a8-3', editable=False, max_length=10, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='logo/images')),
                ('logo', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
