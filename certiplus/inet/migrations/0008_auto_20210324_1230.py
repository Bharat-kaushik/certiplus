# Generated by Django 3.1.7 on 2021-03-24 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inet', '0007_auto_20210323_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='growsection',
            name='color',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
