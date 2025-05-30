# Generated by Django 5.2 on 2025-05-03 17:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0006_alter_room_landlord"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="check_in",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="booking",
            name="check_out",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="booking",
            name="email",
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name="booking",
            name="full_name",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="booking",
            name="phone",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name="booking",
            name="tenant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="myapp.tenant",
            ),
        ),
    ]
