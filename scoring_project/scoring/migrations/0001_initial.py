# Generated by Django 4.2.16 on 2024-10-26 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Scoring",
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
                ("job_LE", models.CharField(max_length=200)),
                ("marital_LE", models.CharField(max_length=200)),
                ("education_LE", models.CharField(max_length=200)),
                ("default_LE", models.CharField(max_length=200)),
                ("housing_LE", models.CharField(max_length=200)),
                ("loan_LE", models.CharField(max_length=200)),
                ("contact_LE", models.CharField(max_length=200)),
                ("month_LE", models.CharField(max_length=200)),
                ("poutcome_LE", models.CharField(max_length=200)),
                ("age", models.IntegerField()),
                ("balance", models.IntegerField()),
                ("day", models.IntegerField()),
                ("duration", models.IntegerField()),
                ("campaign", models.IntegerField()),
                ("pdays", models.IntegerField()),
                ("previous", models.IntegerField()),
            ],
        ),
    ]
