# Generated by Django 5.0.6 on 2024-08-05 08:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_review_user_alter_review_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='ratings',
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.IntegerField(default=0.0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='bookrecommendation',
            name='rating',
            field=models.IntegerField(default=0.0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]