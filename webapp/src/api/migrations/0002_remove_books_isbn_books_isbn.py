# Generated by Django 5.0 on 2023-12-15 03:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='ISBN',
        ),
        migrations.AddField(
            model_name='books',
            name='isbn',
            field=models.IntegerField(default=1, unique=True, validators=[django.core.validators.MinValueValidator(99999999), django.core.validators.MaxValueValidator(9999999999999)], verbose_name='ISBN'),
            preserve_default=False,
        ),
    ]
