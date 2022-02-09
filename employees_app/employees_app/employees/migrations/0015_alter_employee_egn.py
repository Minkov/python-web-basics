# Generated by Django 4.0.1 on 2022-02-08 18:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0014_alter_employee_options_department_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='egn',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='EGN'),
        ),
    ]