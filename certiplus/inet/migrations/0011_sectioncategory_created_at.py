# Generated by Django 3.1.7 on 2021-03-24 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inet', '0010_auto_20210324_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectioncategory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
