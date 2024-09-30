# Generated by Django 5.0.2 on 2024-04-27 20:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipe", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="cuisine",
            field=models.TextField(default="Any kind of cuisine"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="recipe",
            name="number_of_portions",
            field=models.TextField(default="1 person"),
            preserve_default=False,
        ),
    ]
