# Generated by Django 4.1.2 on 2022-10-28 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
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
                ("BrandName", models.CharField(max_length=100)),
                ("ModelName", models.CharField(max_length=100)),
                ("FuelType", models.CharField(max_length=100)),
                ("price", models.FloatField()),
            ],
        ),
    ]