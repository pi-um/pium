# Generated by Django 4.2 on 2024-01-09 10:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("faq", "0002_askinformation"),
    ]

    operations = [
        migrations.AddField(
            model_name="askinformation",
            name="content",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="askinformation",
            name="reg_date",
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="askinformation",
            name="status",
            field=models.CharField(
                choices=[("p", "결제/예약"), ("A", "상담"), ("E", "기타")],
                default="E",
                max_length=1,
            ),
        ),
        migrations.AddField(
            model_name="askinformation",
            name="title",
            field=models.CharField(default="제목 없음", max_length=500),
        ),
        migrations.AddField(
            model_name="askinformation",
            name="use_yn",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="askinformation",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
