# Generated by Django 4.1 on 2022-08-06 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=27, null=True),
        ),
    ]
