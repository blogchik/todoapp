# Generated by Django 4.2.4 on 2023-08-27 10:51

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
                ("title", models.CharField(max_length=150)),
                ("description", models.CharField(blank=True, max_length=300)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("done", models.BooleanField(default=False)),
            ],
        ),
    ]
