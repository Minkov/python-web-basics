# Generated by Django 4.2.10 on 2024-02-12 16:06

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
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
                ("title", models.CharField(max_length=24)),
                ("description", models.TextField()),
                ("is_done", models.BooleanField(default=False)),
            ],
        ),
    ]
