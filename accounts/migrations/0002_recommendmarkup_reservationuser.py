# Generated by Django 4.2 on 2024-01-12 09:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RecommendMarkup",
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
                    "type",
                    models.CharField(
                        choices=[
                            ("SPRINGBRIGHT", "봄 브라이트"),
                            ("SPRINGTRUE", "봄 트루"),
                            ("SUMMERBRIGHT", "여름 브라이트"),
                            ("SUMMERMUTE", "여름 트루"),
                            ("FALLBRIGHT", "가을 브라이트"),
                            ("FALLTRUE", "가을 트루"),
                            ("FALLDEEP", "가을 딥"),
                            ("WINTERBRIGHT", "겨울 브라이트"),
                            ("WINTERDEEP", "겨울 딥"),
                        ],
                        default="SPRINGBRIGHT",
                        max_length=50,
                    ),
                ),
                ("content", models.TextField()),
                ("link", models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="ReservationUser",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=20)),
                (
                    "consultResult",
                    models.CharField(
                        choices=[
                            ("SPRINGBRIGHT", "봄 브라이트"),
                            ("SPRINGTRUE", "봄 트루"),
                            ("SUMMERBRIGHT", "여름 브라이트"),
                            ("SUMMERMUTE", "여름 트루"),
                            ("FALLBRIGHT", "가을 브라이트"),
                            ("FALLTRUE", "가을 트루"),
                            ("FALLDEEP", "가을 딥"),
                            ("WINTERBRIGHT", "겨울 브라이트"),
                            ("WINTERDEEP", "겨울 딥"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "consultResult02",
                    models.CharField(
                        choices=[
                            ("SPRINGBRIGHT", "봄 브라이트"),
                            ("SPRINGTRUE", "봄 트루"),
                            ("SUMMERBRIGHT", "여름 브라이트"),
                            ("SUMMERMUTE", "여름 트루"),
                            ("FALLBRIGHT", "가을 브라이트"),
                            ("FALLTRUE", "가을 트루"),
                            ("FALLDEEP", "가을 딥"),
                            ("WINTERBRIGHT", "겨울 브라이트"),
                            ("WINTERDEEP", "겨울 딥"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                ("reg_date", models.DateField(auto_now=True)),
            ],
            options={
                "verbose_name": "회원관리",
                "verbose_name_plural": "회원관리",
            },
        ),
    ]