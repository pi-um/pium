# Generated by Django 4.2 on 2024-01-09 08:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("faq", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AskInformation",
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
            ],
        ),
    ]
