# Generated by Django 4.1 on 2022-08-18 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_patient_profilepic_alter_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='profilepic',
            field=models.ImageField(upload_to='media/patients/9586'),
        ),
    ]
