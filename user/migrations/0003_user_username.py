# Generated by Django 4.0.6 on 2022-08-06 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_gender_alter_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, null='default username'),
            preserve_default='default username',
        ),
    ]
