# Generated by Django 4.1 on 2022-08-06 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0024_alter_user_options'),
        ('appointment', '0004_appointment_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointed', to='user.patient'),
        ),
    ]
