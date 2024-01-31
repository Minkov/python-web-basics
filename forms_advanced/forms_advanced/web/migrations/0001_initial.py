# Generated by Django 4.2.9 on 2024-01-31 16:20

from django.db import migrations, models
import forms_advanced.web.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        max_length=32,
                        validators=[forms_advanced.web.models.validate_first_name],
                    ),
                ),
            ],
        ),
    ]
