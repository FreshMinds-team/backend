# Generated by Django 4.1 on 2022-08-06 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0027_user_address_alter_user_phone'),
        ('medication', '0002_medication_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicine', to='user.patient'),
        ),
    ]